from sklearn import linear_model
import pandas as pd
from sklearn.feature_selection import RFE
from itertools import compress
from sklearn.model_selection import train_test_split


Wait_Data_df = pd.read_excel("WaitData.Published.xlsx")
Wait_Data = Wait_Data_df.drop(columns=['x_ArrivalDTTM', 'x_ScheduledDTTM', 'x_BeginDTTM'])
print(len(Wait_Data.columns.tolist()))
y_col = 'Wait'
feature_cols = [x for x in Wait_Data.columns if x != y_col]
X_data = Wait_Data[feature_cols]
print(len(X_data.columns.to_list()))
y_data = Wait_Data[y_col]
name_col = []
ID=[]
Min =[]
model = linear_model.LinearRegression()


def main():

   for i in range(0,3):
     select_fetures(i)
   print(name_col)
   print(ID)
   print(Min)
   ID.clear()
   Min.clear()
   name_col.clear()
   for i in range(0,15):
     select_fetures(i)
   print(name_col)
   print(ID)
   print(Min)
   for i in range (0,15):
       if(Min[i][1]< 24 ):
           min_feature=i
           break
   print(min_feature+1)

def select_fetures(num):
    info=[]
    min=10000
    for i in range(0, len(X_data.columns) - 1):
        if (i in ID):
            continue
        name_col.append(X_data.columns[i])
        model.fit(X_data[name_col], y_data)
        Ypred = model.predict(X_data[name_col])  # use trained regression model to predict
        r = y_data - Ypred  # compute prediction error (residual)
        e = abs(r).mean()  # compute model error
       # print("the error for " + str(i) + " is " + str(e))
        name_col.remove(X_data.columns[i])
        if (min > e):
            min = e
            id = i
    ID.append(id)
    temp =(num , min)
    Min.append(temp)
    name_col.append(X_data.columns[id])


if __name__ == '__main__':
    main()



'''
 print(X_data[i].tolist())
 bb=X_data[i].astype(float).tolist()
 break

model.fit(X_data, y_data)
Ypred = model.predict(X_data) # use trained regression model to predict
r = y_data-Ypred # compute prediction error (residual)
e = abs(r).mean() # compute model error
print(str(e))
print(abs(r).median())




min1 =100000
for i in range(0,len(X_data.columns)-1):

    name_col.append(X_data.columns[i])
    model.fit(X_data[name_col], y_data)
    Ypred = model.predict(X_data[name_col])  # use trained regression model to predict
    r = y_data - Ypred  # compute prediction error (residual)
    e = abs(r).mean()  # compute model error
    print("the error for "+str(i)+" is "+str(e))
    name_col.remove(X_data.columns[i])
    if(min1 > e):
        min1=e
        id1=i
   #     print (str(min))
    #    print(str(id))

print (" min is "+str(min1)+" with id "+str(id1) +" the name is "+X_data.columns[id1])
min2=10000
name_col.append(X_data.columns[id1])
for i in range(0,len(X_data.columns)-1):
    if(i==id1):
        continue
    name_col.append(X_data.columns[i])
    model.fit(X_data[name_col], y_data)
    Ypred = model.predict(X_data[name_col])  # use trained regression model to predict
    r = y_data - Ypred  # compute prediction error (residual)
    e = abs(r).mean()  # compute model error
    print("the error for "+str(i)+" is "+str(e))
    name_col.remove(X_data.columns[i])
    if(min2 > e):
        min2=e
        id2=i
   #     print (str(min))
    #    print(str(id))
print (" min is "+str(min2)+" with id "+str(id2) +" the name is "+X_data.columns[id2])
name_col.append(X_data.columns[id2])

min3=10000
for i in range(0,len(X_data.columns)-1):
    if(i==id1 or i == id2):
        continue
    name_col.append(X_data.columns[i])
    model.fit(X_data[name_col], y_data)
    Ypred = model.predict(X_data[name_col])  # use trained regression model to predict
    r = y_data - Ypred  # compute prediction error (residual)
    e = abs(r).mean()  # compute model error
    print("the error for "+str(i)+" is "+str(e))
    name_col.remove(X_data.columns[i])
    if(min3 > e):
        min3=e
        id3=i
   #     print (str(min))
    #    print(str(id))
print (" min is "+str(min3)+" with id "+str(id3) +" the name is "+X_data.columns[id3])
name_col.append(X_data.columns[id3])
print(name_col)
'''