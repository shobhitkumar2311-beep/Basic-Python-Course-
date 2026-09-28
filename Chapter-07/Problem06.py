# Write a program to calculate the factorial of a given number using for loop. 
# Taking input by the user
number = int(input("Entre the number: "))
product = 1
for i in range(1,number+1):
    product = product * i
print(f"The factorial of {number} is: ",product)