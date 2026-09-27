# Write a python program to print the contents of a directory using the os module. Search online for the function which does that. 

# Program to print contents of a directory using os module
import os

# specify the directory path
directory_path = r"C:\Users\ASUS\OneDrive\Desktop\Python-Course-Basic\Chapter-01"

# list all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory in the contents
for item in contents:
    print(item)