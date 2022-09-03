
import glob
import os

def print_youngest_Male():
    folderPath = ["Elr-ExampleMessages-1.9.2-012216", "Immunization-ExampleMessages-1.9-021214",
                  "Syndromic-ExampleMessages-1.6-081313", "Older"]
    youngestDate = 0
    i = 0
    for item in folderPath:
        for filename in glob.glob(os.path.join(item, '*.*')):
            with open(filename, 'r') as f:
             #   line = f.readline()
                cnt = 1
                for line in f:
                    strArray = line.split("|")
                    if (strArray[0] == "PID" and strArray[8] == "M" and strArray[7] != ""):
                        tempDate = strArray[7]
                        stringbirthDate = tempDate[0:4]
                        intDate = int(stringbirthDate)
                        if (youngestDate < intDate):
                            youngestDate = intDate
                        break

    print("The year was the youngest male patient born " + str(youngestDate))

def print_count_female():
    folderPath = ["Elr-ExampleMessages-1.9.2-012216", "Immunization-ExampleMessages-1.9-021214",
                  "Syndromic-ExampleMessages-1.6-081313", "Older"]
    countUnigueFemale = 0
    womenList = []
    i = 0
    for item in folderPath:
        for filename in glob.glob(os.path.join(item, '*.*')):
            with open(filename, 'r') as f:
            #    line = f.readline()
                cnt = 1
                for line in f:
                    strArray = line.split("|")
                    if (strArray[0] == "PID" and (strArray[8] == "F" or strArray[8] == "F\n")):
                        if(strArray[5] not in womenList ):
                            womenList.append(strArray[5])
                            countUnigueFemale+=1

    print("The number of unique female patients is " + str(len(womenList)))
    print(womenList)



if __name__ == '__main__':
    print_youngest_Male()
    print_count_female()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
