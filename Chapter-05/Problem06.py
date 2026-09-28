# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 
Dictionary = {}

Name = input("Enter your name: ")
Language = input("Enter your favorite language: ")
Dictionary[Name] = Language
Name = input("Enter your name: ")
Language = input("Enter your favorite language: ")
Dictionary[Name] = Language
Name = input("Enter your name: ")
Language = input("Enter your favorite language: ")
Dictionary[Name] = Language
Name = input("Enter your name: ")
Language = input("Enter your favorite language: ")
Dictionary[Name] = Language

print("The favorite languages of friends are:", Dictionary)