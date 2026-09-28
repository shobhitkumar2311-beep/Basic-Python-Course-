# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’. 

# Open the files
f = open("Chapter-09\poem.txt", "r")
# Read the file
content = f.read()
# Taking the value by the user
value = input("Enter the word: ")
# Checking the condition in the file
if value in content.lower() :
    print(f"{value} is present in the file")
else:
    print(f"{value} is not present in the file")
# File will be close
f.close()
