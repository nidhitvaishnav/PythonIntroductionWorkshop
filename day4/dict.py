dict1 = {"uName":"utd1234", "pword":"abc789Xyz"}
# print(dict1["uName"])

for key in dict1:
    print(dict1[key])
for key, value in dict1.items():
    print(key, ":", value)

dict1["pword"]="xyz987Abc"
print(dict1["pword"])