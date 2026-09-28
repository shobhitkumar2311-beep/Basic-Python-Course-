# Write a program to print the following star pattern. 
'''
* 
*** 
*****  for n = 3 '''
# Taking value by the user
n = int (input("Enter the value: "))
# Strating loop for printing the star pattren
for i in range(1,n+1):
    print("*"* (2*i-1), end="") # In this statement when i=1 then star=1 then change the star according to the i for changing the shape 
    print("")