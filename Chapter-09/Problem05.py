# Repeat program 4 for a list of such words to be censored.

# Ask user for input
choice = input("Do you want to replace the word or reverse the content? (yes/no): ")
words = ["donkey", "the", "is", "a", "with"]
# Read the file
with open("Chapter-09/donkey02.txt", "r") as f:
    content = f.read()
if choice == "yes":
    # Replace operation
    for word in words:
        content = content.replace(word, "#" * len(word))
    # Rewrite the file
    with open("Chapter-09/donkey02.txt", "w") as f:
        f.write(content)
    print("✅ Words replaced successfully!")
elif choice == "no":
    # Reverse operation
    for word in words:
        content = content.replace("#" * len(word), word)
    # Rewrite the file
    with open("Chapter-09/donkey02.txt", "w") as f:
        f.write(content)
    print("🔄 Word restored successfully!")
else:
    print("⚠️ Invalid input! Please type 'yes' or 'no'.")