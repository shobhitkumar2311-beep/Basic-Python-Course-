# Write a program which finds out whether a given name is present in a list or not.
Dictionary = ["Shobhit","Pooja","Rohit","Ankit","Ramesh","Suresh","Rakesh","Sakshi","Ankita","Shivam"]
#Taking input from the user
Name = input("Enter the name to checking in the list: ")
if(Name in Dictionary):
    print("The name is present in the list.")
else:
    print("The name is not found in the list.")