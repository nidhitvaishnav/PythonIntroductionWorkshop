list1=["Black Panther","Captain America","Peter Rabbit","Thor Ragnorak"]
print(list1)

#add item at the end of list
list1.append("Early Man")
print(list1)

#inserts item at given index
list1.insert(2,"Avengers")
print(list1)

#find the index of current list
h=list1.index("Thor Ragnorak")
print(h)

#remove the item from the list, if item does not exist, it will give error saying item not in list
list1.remove("Peter Rabbit")
print(list1)

#reverse the list
list1.reverse()
print(list1)

#sort the list
list1.sort()
print(list1)
