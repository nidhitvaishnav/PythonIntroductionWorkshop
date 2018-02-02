name = input("Enter your name: ")
if name.islower():
    print ("You have entered your name in lower case.")
elif name.isupper():
    print ("You have entered your name in upper case.")
else:
    print("You have entered your name in both upper and lower case.")

print("{} in lower case is {}.".format(name, name.lower()))
print("{} in upper case is {}".format(name, name.upper()))