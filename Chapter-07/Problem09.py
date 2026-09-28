# Write a program to print the following star pattern. 
'''
* * * 
*   *     
* * *
for n = 3'''
# Taking value by the user
n = int (input("Enter the value: "))
# Strating loop for printing the star pattren
for i in range(1,n+1):
    if(i==1 or i==n): # This statement will be working on first and last line.
        print("*"*n,end="")
    else: # This statement will be working when i & n both are diffrent values.
        print("*", end="")  # This is define first colum
        print(" "*(n-2), end="") # This define the space area detween the daigram.
        print("*", end="")  # This is define last colum
    print("")