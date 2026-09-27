# Check the type of variable assigned using input () function.
a = input("Enter a value: ")
try:
    a=int(a) # This is checking the value in integer format
    print("The value of a is integer and the value is ",a)
except ValueError:
    try: 
        a=float(a) # This is checking the value in float format
        print("The value of a is float and the value is ",a)
    except ValueError:
        pass #This is checking the value in string format
        print("The value of a is string and the value is ",a)
