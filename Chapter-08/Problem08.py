#  Write a python function to print multiplication table of a given number.

# Creating the function

# Function
def multiplication(n): 

# loop
    for i in range(1,11): 

# Calculating the table
        print(f"{n} X {i} = {n*i}") 

# Taking the input by the user
n = int (input("Enter the value for calculating the table: "))

# Calling the function
multiplication(n) 