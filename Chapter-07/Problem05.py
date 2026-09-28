# Write a program to find the sum of first n natural numbers using while loop.

# Taking a number by the user
number = int(input("Enter the n natural number: "))
# While loop will be strated
i = 1
sum = 0 
while(i<=number):
    sum = sum + i
    i += 1

print("Sum first ",number," natural number is given as: ",sum)
