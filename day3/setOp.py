list1 = map(str, input("Enter name of cityList1: ").split())
list2 = map(str, input("Enter name of cityList2: ").split())

set1 = set(list1)
set2 = set(list2)

unionSet = set1|set2
intersectionSet = set1 & set2
exOrSet = set1 ^ set2
subtractionSet = set1 - set2

print("union set: {}".format(unionSet))
print("intersection set: {}".format(intersectionSet))
print("exOrSet : {}".format(exOrSet))
print("subtractionSet: {}".format(subtractionSet))