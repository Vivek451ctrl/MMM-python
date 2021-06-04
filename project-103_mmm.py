import csv 
from collections import Counter




with open("data.csv", newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)
    
#print(fileData)
#poping out the column names

fileData.pop(0)

newData = []
for i in range(len(fileData)):
    newData.append(float(fileData[i][2]))
#calculating mean!!
mean = sum(newData)/len(newData)
print(f"the mean of the list is :{mean}")

#calculating meadian
newData.sort()
length = len(newData)
if length%2 == 0:
    median1 = float(newData[length//2])
    median2 = float(newData[length//2-1])
    median = (median1+median2)/2

else:
    median = newData[length//2]
    
print(f"the median = {median}")

#calculating mode
data = Counter(newData)
print(data)
maxNumber = 0

for key, val in data.items():
    if val>maxNumber:
        maxNumber = val
        mode = float(key)
    
print(f"mode is {mode}")