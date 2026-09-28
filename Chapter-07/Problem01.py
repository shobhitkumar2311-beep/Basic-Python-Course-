# Write a program to print multiplication table of a given number using for loop.
 
# Get the number from the user
number = int(input("Enter a number to print its multiplication table: "))
#use for loop to iterate from 1 to 10 and print the multiplication table
for i in range(1,11):
    print(f"{number} X {i} = {number*i}")