import ply.lex as lex
import ply.yacc as yacc
import re
import sys

And = r"/\\"
Or = r"\\/"
tokens = [
    'VARIABLE','AND','OR','IMPL','NEG', 'OB',
    'CB'
]
t_VARIABLE = r'[a-zA-Z]'
t_AND= r'\/\\'
t_OR= r'\\/'
t_IMPL =r'\->'
t_NEG= r'\!'
t_OB=r'\('
t_CB=r'\)'

t_ignore = r' '


def t_error(t):
    print("Illegal characters! ")
    t.lexer.skip(1)


lexer=lex.lex()

def p_Boolean(p):
    '''
        Boolean : expression
                | factor
                | empty

    '''

    l=p[1]
    print(l)
    l=CNF_fun(p[1])
    print(l)
    s = l
    s = re.sub("\s", '', s)
    s = re.sub("!!", '', s)
    s = re.sub("\(", '', s)
    s = re.sub("\)", '', s)
    x = PL_Resolution(s)
    print(x)
  #  try:
   #  if(len(l)!=0):print(l)
   # except EOFError: print("error")


def p_expression_norm(p):
    '''
    expression :  OB expression CB
    '''
    p[0] = p[2]
    #print(p[0])
def p_expression(p):
    '''
    expression : expression AND expression

    '''


    p[0] = p[2],p[1] ,p[3]
   # print(p[0])
def p_expression_factor(p):
    '''
    expression : factor AND expression
               | expression AND factor

    '''
    p[0] = p[2],p[1] ,p[3]



def p_expression_fact(p):
    '''
    expression : factor OR factor
               | factor AND factor
               | factor IMPL factor

    '''

    p[0] = p[2], p[1], p[3]
   # print(p[0])


    #print(p[0])
def p_factor(p):
    '''
    factor : VARIABLE
    '''
    p[0] = p[1]
   # print(p[0])
def p_factor_not(p):
    '''
    factor : NEG VARIABLE
    '''
    p[0] = p[1], p[2]
   # print(p[0])

def p_error(p):
    done= False
    print("Syntax Error")

def p_empty(p):
    '''
        empty :
    '''
    p[0]=None
   # print(p[0])

def CNF_fun (p):
    if(type(p) == tuple):
        if (p[0] == '->'):
              return '('+'!' + CNF_fun(p[1]) + '\/' +CNF_fun(p[2])+')'
        elif (p[0] == '/\\'):
            return '('+CNF_fun(p[1]) + '/\\' + CNF_fun(p[2])+')'
        elif (p[0] == '\/'):
            return '('+CNF_fun(p[1]) + '\/' + CNF_fun(p[2])+')'
        elif (p[0] == '!'):
            return '!' + CNF_fun(p[1])
    else:
        return  p

def PL_Resolution(s):

    if(len(s) <= 2 ):
        return True
    else:
     clauses = re.split(And,s)
    # if (len(clauses) < 2):
    #     return True

     result = check(clauses)
     if (result == '-'):
         return False

     resolve_set = PL_Resolve(clauses[0], clauses[1])
     if(len(clauses)==2):
      result = check(clauses)
      if (result == '-'):
             return False
      result = check_or(resolve_set)
      if (result == '+'):
         return True
      if (result == '-'):
         return False

     iteration=0
     new =[]
     while(True):
         iteration+=1
         for i in range(len(clauses)):
             for j in range(i,len(clauses)):
                 if (i == j): continue
                 resolve_set = PL_Resolve(clauses[i],clauses[j])
                 if(resolve_set is not None):
                     if(resolve_set not in new):
                         new.append(resolve_set)
                        # clauses.append(resolve_set)
         result = check(new)
         if(result == '-'):
             return False

         clauses.extend(new)
         if(iteration==20):
             print("+")
             return



def PL_Resolve(clause1,clause2):
    new_clause=[]
    c1=re.split(Or , clause1)
    c2=re.split(Or , clause2)
    for i in range(len(c1)):
        if (re.findall('!', c1[i])):
            temp = re.sub('!', '', c1[i])
        else:
            temp= '!' + c1[i]
        for j in range(len(c2)):
            if (temp == c2[j]):
                c1.remove(c1[i])
                c2.remove(c2[j])


                if(len(c1)==0):
                    x2 = c2.pop()
                    y = x2
                elif(len(c2)==0):
                    x1 = c1.pop()
                    y = x1
                else:
                    x1 = c1.pop()
                    x2 = c2.pop()
                    if(x1 == x2):
                        y = x1
                    else:
                        if (re.findall(x1, x2)):
                            y = x1
                        else:
                         y = x1 + "\\/" + x2
                new_clause=y
                return new_clause




def check(s):
   # s1=w
   # s= s1.pop()
    x='$'
    if ((("p" in s) and ("!p" in s)) or ("!p/\p" in s) or ("p/\!p" in s)):
        x= '-'
    elif ((("q" in s) and ("!q" in s))or ("!q/\q" in s) or ("q/\!q" in s)):
        x=  '-'
    elif ((("s" in s) and ("!s" in s))or ("!s/\s" in s) or ("s/\!s" in s)):
        x= '-'
    if ((("r" in s) and ("!r" in s)) or ("!r/\\r" in s) or ("r/\!r" in s)):
        x= '-'
    elif ((("t" in s) and ("!t" in s))or ("!t/\\t" in s) or ("t/\!t" in s)):
        x=  '-'
    return x
def check_or(s):
    x ='$'
    if (("p\/!p" in s) or ("!p\/p" in s) or ("p" in s) or ("!p" in s) ):
     x = '+'
    elif (("q\/!q" in s) or ("!q\/q" in s) or ("q" in s) or ("!q" in s) ):
     x = '+'
    elif (("s\/!s" in s) or ("!s\/s" in s) or ("s" in s) or("!s" in s)):
      x = '+'
    elif (("r\/!r" in s) or ("!r\/r" in s) or ("r" in s) or("!r" in s)):
      x = '+'
    elif(("t\/!t" in s) or ("!t\/t" in s) or ("t" in s) or("!t" in s)):
     x = '+'
    elif(("!p\/!p" in s) or("!q\/!q" in s) or ("!s\/!s" in s) or ("!r\/!r" in s) or ("!t\/!t" in s)):
     x='-'
    return x



parser=yacc.yacc()

#lexer.input(s)

while (True):
        l=[]
        try:
            s = input('>>')
        except EOFError:
            break
        if not s: continue
        parser.parse(s)
       # print(m)

'''

result=check_or(clauses)
     if (result == '+'):
         return True
     elif(result== '-'):
         return False
'''