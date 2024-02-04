def doCompare(first, second, third) :

# Using Ternary operator (cleaner)
#    largest = (first if (first > second and first > third) else
#               (second if (second > first and second > third) else third))
#    return largest
    
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
# Running the doCompare function, passing the inputs as parameters
largest = doCompare(first, second, third)
# Got the returned largest result, and sending it to output
print("The largest number of those three is:", largest)
