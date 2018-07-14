list1=[5,10,7,9,2]

#len(listName) finds length of list (total items in the list)
w=len(list1)
print(w)

print("in list")
for item in list1:
    print(item)

print("for loop from 0 to size of list which gives index of list")
print("based on it we are accessing items")
for index in range(0,w):
    print(index,list1[index])

print("no need to find index, enumerate will automatically do that for us")
for index, item in enumerate(list1):
    print(index, item)

