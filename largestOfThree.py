def doCompare(first, second, third) :
  
    # Using Nested if statements
    if first > second:
        if first > third :
            largest = first
        else:
            largest = third
    else:
        if second > third :
            largest = second
        else:
            largest = third
    return largest

# Have to convert/cast the input to either integer or float or it won't work properly
first = float(input("Enter First Number: "))
second = float(input("Enter Second Number: "))
third = float(input("Enter third Number: "))
# Running the doCompare function, passing the inputs as parameters, saving the returned value into
# the largest variable
largest = doCompare(first, second, third)
# Got the returned largest result, and sending it to output
print("The largest number of those three is:", largest)
