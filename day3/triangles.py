n = int(input("For how many lines do you want the pattern: "))

# top left corner right angle
for i in range (n, 0, -1):
    for j in range(i):
        print("# ", end="")
    # for j -ends
    print("")
# for i -ends

print ("")


# bottom left corner right angle
for i in range(1, n+1):
    for j in range(i):
        print("* ", end="")
    # for j -ends
    print("")
# for i -ends

print ("")



# equal side triangle
for i in range(1,n+1):
    for j in range(n-i):
        print(end=" ")
    # for j -ends
    for j in range(i):
        print ("% ", end="")
    # for i -ends
    print("")
# for i -ends

print ("")

# top right corner as right angle
for i in range(1, n+1):
    for j in range(i):
        print(" ", end="")
    #for j -ends
    for j in range(n+1-i):
        print("$", end="")
    # for j -ends
    print("");
# for i -ends

print ("")

# ottom right corner as right angle
for i in range (1, n+1):
    for j in range(n-i):
        print (" ", end= "")
    #for j -ends
    for j in range(i):
        print("@", end = "")
    #for j -ends
    print("")
#for i -ends


