numList = list(map(int, input("Enter numbers: ").split()))

print(numList.__class__)
print (numList)
numSet = set(numList)

print("Non - duplicate values : {}".format(numSet))

minVal = numList[0]
maxVal = numList[0]
for i in numList:
    if i>maxVal:
        maxVal=i
    #if numList -ends
    if i<minVal:
        minVal=i
    #if numList -ends
#for i -ends

print("min value = {}, max value = {}".format(minVal, maxVal))