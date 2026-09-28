# Write a python function to remove a given word from a list ad strip it at the same time. 
# Creating te function
def rem(l, word):
    n = []                  # Empty dictionary
    for item in l:          # Creating loop
        if not ( item == word ): 
            n.append ( item.strip (word) ) # Searching the word in the dictionary by the help of loop 
    return n                # returning the excet value

l = ["Herry","an","Shobhit","Rohan","an" ] # This is creating the list by the system

print(rem(l,"an"))          # Print the output




# Creating to function
def rem(l, word):
    for item in l:
        l.remove(word)      # Creating loop
        return l            # returning the excet value 

l = ["Herry","an","Shobhit","Rohan","an" ] # This is creating the list by the system

print(rem(l,"an"))          # Print the output