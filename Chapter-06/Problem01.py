# Write a program to find the greatest of four numbers entered by the user. 

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

# Finding the greatest number
if(num1>=num2)and(num1>=num3)and(num1>=num4):
    greatest = num1
    print("The greatest number is:",greatest)
elif(num2>=num1)and(num2>=num3)and(num2>=num4):
    greatest = num2
    print("The greatest number is:",greatest)
elif(num3>=num1)and(num3>=num2)and(num3>=num4):
    greatest = num3
    print("The greatest number is:",greatest)
else:
    greatest = num4
    print("The greatest number is:",greatest)
