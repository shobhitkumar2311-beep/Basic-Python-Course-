# Can you change the values inside a list which is contained in set S?  
    # s = {8, 7, 12, "Harry", [1,2]}


# This statement will give an {(1, 2), 'Harry', 7, 8, 12} 
s = {8, 7, 12, "Harry", (1,2)}
print(s)

# This statement will give an error because list is mutable and cannot be added to a set.
s = {8, 7, 12, "Harry", [1,2]}
print(s)
