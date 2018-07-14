'''
Check whether the input name has only alphabets, numeric or both

For caseConditionCode:
just use islower() / isupper() instead of isalpha() or isnumeric()
'''


name = input("Please enter your user name: ")
if (name.isalpha()):
    print(name, "contains only alphabets.")

elif(name.isnumeric()):
    print(name, "contains only numbers.")

else:
    print(name, "contains alpha numeric")