# Write a program to store seven fruits in a list entered by the user
fruits = [] # This will create an empty list to store the fruits
for i in range(7): #This show the range of the loop to 7
    fruit = input("Enter a fruit: ") 
    fruits.append(fruit) # This will add the fruit name to the list
print("The list of fruits is:", fruits)