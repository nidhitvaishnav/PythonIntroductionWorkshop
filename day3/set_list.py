'''
list: square brackets
'''
list = [2435,324565,2453,234,2, 234]
print(type(list))
print(list)

# print item of the list
print("2nd item in list:", list[1])
# change the value of 1 item from the list
list[1]=-1
print("2nd item in list:", list[1])

print("iterating over list")
for i in range(len(list)):
    print(list[i])
#for i -ends

print("Enumerating over list")
# enumerate will provide index value pair
for index, value in enumerate(list):
    print(index, value)

'''
set
'''
set1 = set(list)
print("set1:",set1)
print("set1 type: ",type(set1))
list = []
print("after making list as an empty list: ",list)
