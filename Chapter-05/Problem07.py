#  If the names of 2 friends are same; what will happen to the program in problem 6?

# The answer is fisrt name will be skip and second name will be execute
'''
Enter your favorite language: python
Enter your favorite language: java
Enter your favorite language: c++
Enter your favorite language: cpp
The favorite languages of friends are: {'Shobhit': 'c++', 'Pooja': 'cpp'}'''

Dictionary = {}

Name = "Shobhit" 
Language = input("Enter your favorite language: ")
Dictionary[Name] = Language
Name = "Pooja"
Language = input("Enter your favorite language: ")
Dictionary[Name] = Language
Name = "Shobhit"
Language = input("Enter your favorite language: ")
Dictionary[Name] = Language
Name = "Pooja"
Language = input("Enter your favorite language: ")
Dictionary[Name] = Language

print("The favorite languages of friends are:", Dictionary) 