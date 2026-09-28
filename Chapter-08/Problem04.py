# Write a recursive function to calculate the sum of first n natural numbers. 

'''
sum(0) = 0
sum(1) = 1
sum(2) = 1+2
sum(3) = 1+2+3
sum(4) = 1+2+3+4
sum(5) = 1+2+3+4+5
sum(n) = n+sum_number(n-1)
'''
def sum_natural_number(number):
    if(number==0):
        return 0
    else:
        return number + sum_natural_number(number-1)
    
    
# Input from user
number = int(input("Enter the number for the sum of n natural numbers: "))

# Output result
print("Sum of first", number, "natural numbers is:", sum_natural_number(number))
