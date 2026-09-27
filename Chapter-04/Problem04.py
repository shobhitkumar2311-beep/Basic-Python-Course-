# Write a program to sum a list with 4 numbers.
Numbers = [] # This will create an empty list to store the numbers
for i in range (4): #This show the range of the loop to 4
    number = int (input("Enter number: "))
    Numbers.append(number) # This will add the number to the list
print("The sum of the numbers is:", sum(Numbers))