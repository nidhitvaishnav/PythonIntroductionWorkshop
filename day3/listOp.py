myList = [10,20,30]
print(myList)

myList.insert(0,5)
print(myList)

myList.insert(1,10)
print(myList)

myList.insert(4,6)
print(myList)

# myList.insert(-1, "hi")
# print(myList)

myList.remove(6)
print(myList)

myList.append(9)
print(myList)

myList.append(1)
print(myList)

myList.reverse()
print(myList)

count10=myList.count(10)
print(count10)

index1 = myList.index(1)
print(index1)

myList.pop()
print(myList)

myList.extend([200,100])
print(myList)


myList.sort()
print(myList)

tempList = myList.copy()
print(myList)
print(tempList)
