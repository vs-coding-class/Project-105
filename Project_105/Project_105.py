import math
import csv

with open('standardDeviation.csv') as f:
    reader = csv.reader(f)
    fileData = list(reader)

#fileData.pop(0)

data = fileData[0]

def mean():
    totalSum = 0
    dataLength = len(data)

    for x in data:
        totalSum += int(x)

    return totalSum/dataLength;

def standardDeviation():
    #elements = []
    numeratorPart = 0

    for y in data:
        numeratorPart += (int(y) - mean())**2
        print(numeratorPart)
        #numeratorPart = numeratorPart**2
        #elements.append(numeratorPart)
    
    #for z in elements:
        #numerator += z
    
    standardDeviation = math.sqrt(numeratorPart/len(data))
    print(f"The standard deviation of this data set is {standardDeviation}.")

standardDeviation()