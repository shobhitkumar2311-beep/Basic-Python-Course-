# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file

# Ask user for input
choice = input("Do you want to replace the word or reverse the content? (yes/no): ")

# Read the file
with open("Chapter-09\donkey01.txt", "r") as f:
    content = f.read()
if choice == "yes":
    # Replace operation
    content_new = content.replace("donkey","####")
    # Rewrite the file
    with open("Chapter-09\donkey01.txt", "w") as f:
        f.write(content_new)
    print("✅ Word 'donkey' replaced with '####' successfully!")
elif choice == "no":
    # Reverse operation
    content_reversed = content.replace("####","donkey")
    # Rewrite the file
    with open("Chapter-09\donkey01.txt", "w") as f:
        f.write(content_reversed)
    print("✅ Word 'donkey' replaced with '####' successfully!")
else:
    print("⚠️ Invalid input! Please type 'yes' or 'no'.")