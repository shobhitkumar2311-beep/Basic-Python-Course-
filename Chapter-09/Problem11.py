# Write a python program to rename a file to “renamed_by_ python.txt

# Taking input by the user
you = int(input("Enter the value: "))

# In the file you enter 1 then make a new file "new_by_python.txt"
if (you == 1):

    # Reading the file
    with open("Chapter-09/old.txt") as f:
        content = f.read()

    # Rename the file by the help of python.
    with open("Chapter-09/new_by_python.txt", "w") as f:
        f.write(content)

# In the file you enter 2 then new file will be "new_by_python.txt" deleted.
elif(you == 2):

    import os
    # Original file path
    file_path = "Chapter-09/new_by_python.txt"

    # Check if the file exists before deleting
    if os.path.exists(file_path):
        os.remove(file_path)
        print("🗑️ File deleted successfully!")

    else:
        print("⚠️ File not found.")

# In the file you enter 3 then "old.txt" file will be deleted and new file maked "renamed_by_python.txt"
elif(you == 3):

    import os
    # Original file path
    old_name = "Chapter-09/old.txt"

    # New file name (renamed)
    new_name = "Chapter-09/renamed_by_python.txt"

    # Rename the file
    os.rename(old_name, new_name)

    print("✅ File renamed successfully!")

# In the file you enter 4 then "renamed_by_python.txt" file will be deleted and new file maked "old.txt"
elif(you == 4):

    import os
    # Original file path
    old_name = "Chapter-09/renamed_by_python.txt"

    # New file name (renamed)
    new_name = "Chapter-09/old.txt"

    # Rename the file
    os.rename(old_name, new_name)

    print("✅ File renamed successfully!")

else:
    
    print("Something went wrong please enter the correct value!")