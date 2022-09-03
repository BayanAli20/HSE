import glob
import os

folderPath = ["Immunization-ExampleMessages-1.9-021214"]
youngestDate=0
i=0
countUnigueFemale = 0
womenList = []
for item in folderPath:
    for filename in glob.glob(os.path.join(item, '*.*')):
        with open(filename, 'r') as f:
           # line = f.readline()
            cnt = 1
            for line in f:
                strArray = line.split("|")
                if (strArray[0] == "PID" and (strArray[8] == "F" or strArray[8] == "F\n")):
                    if (strArray[5] not in womenList):
                        womenList.append(strArray[5])
                        countUnigueFemale += 1



print("The year was the youngest male patient born"+ str(youngestDate))
