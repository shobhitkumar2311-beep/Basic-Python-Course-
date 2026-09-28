# Write a program to find whether a given number is prime or not.

# Taking number by the user
number = int(input("Enter the number: "))
 
for i in range(2,number):
    if(number%i)==0:
        print("Number is not prime.")
        break
else:
        print("Number is prime")

# Extra code
division = number % i
print(division)
print(i)