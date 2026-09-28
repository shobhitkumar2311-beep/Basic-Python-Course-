# If languages of two friends are same; what will happen to the program in problem 6?

# The answer is all name will be appaer and make set in the dictionary
'''
Enter your name: Shobhit
Enter your name: Pooja
Enter your name: Rajesh
Enter your name: umesh
The favorite languages of friends are: {'Shobhit': 'Python', 'Pooja': 'Java', 'Rajesh': 'Python', 'umesh': 'Java'}'''

Dictionary = {}

Name = input("Enter your name: ")
Language = "Python"
Dictionary[Name] = Language
Name = input("Enter your name: ")
Language = "Java"
Dictionary[Name] = Language
Name = input("Enter your name: ")
Language = "Python"
Dictionary[Name] = Language
Name = input("Enter your name: ")
Language = "Java"
Dictionary[Name] = Language

print("The favorite languages of friends are:", Dictionary)