# Write a program to print multiplication table of n using for loops in reversed order. 
# Get the number from the user
number = int(input("Enter a number to print its multiplication table: "))
#use for loop to iterate from 1 to 10 and print the multiplication table
for i in range(1,11):
    # For the reversed loop we are using the (last range - i) 11-1 at the place of i.
    print(f"{number} X {11-i} = {number*(11-i)}")
    