# Write a python program to calculate the square of a number entered by the user.
a = input("Enter a number: ")
# In this statement we are given the number by the user.
result = int(a) *int(a)
# This is calculating the square of a number entered by the user.
print("The square of",a,"is",result)
# Another method to calculate the square of a number entered by the user.
result = int(a) **2
print("The square of",a,"is",result,"using another method.")