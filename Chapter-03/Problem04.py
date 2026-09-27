# Replace the double space from problem 3 with single spaces.  
string = input("Enter a string:")
if "  " in string:
    print("The string contains double space.")
    string = string.replace("  "," ")
    print("The string after replacing double space with single space is:\n",string)
else:
    print("The string does not contain double space.")