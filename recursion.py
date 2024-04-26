print("------------Prints nine-----------------")

# recursion is when a function calls itself
def add_one(num): # one parameter 

    # inside function continous until >= 9
    if num >= 9:
        # ends program when true, does this 
        return num + 1
    
    # this is only created, if "num" is less thsn < 9
    total = num + 1
    print(total)

    # this is only happens if "num" is less thsn < 9
    return add_one(total) # recursive call

# call function
add_one(0)

print()
print("------------Prints ten-----------------")
# recursion is when a function calls itself
def add_one(num): # one parameter 

    # inside function continous until >= 9
    if num >= 9:
        # ends program when true, does this 
        return num + 1
    
    # this is only created, if "num" is less thsn < 9
    total = num + 1
    print(total)

    # this is only happens if "num" is less thsn < 9
    return add_one(total) # recursive call

# variable save value from call function 
mynewtotal = add_one(0)
print(mynewtotal)

print("------------importance of return to Prints ten-----------------")
# recursion is when a function calls itself
def add_one(num): # one parameter 

    # inside function continous until >= 9
    if num >= 9:
        # ends program when true, does this 
        return num + 1
    
    # this is only created, if "num" is less thsn < 9
    total = num + 1
    print(total)

    # this is only happens if "num" is less thsn < 9
    add_one(total) # recursive call

# call function
mynewtotal = add_one(0)
print(mynewtotal)

print("------------   -----------------")
print("------------   -----------------")
print("------------   -----------------")
print("------------   -----------------")
print("------------   -----------------")
print("------------   -----------------")
print("------------   -----------------")
print("------------   -----------------")
print("------------   -----------------")
print("------------   -----------------")
print("------------   -----------------")
print("------------   -----------------")
print("------------   -----------------")
print("------------   -----------------")
print("------------   -----------------")
print("------------   -----------------")
print("------------   -----------------")
