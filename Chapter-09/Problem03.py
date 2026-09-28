# Write a program to generate multiplication tables from 2 to 20 and write it to the  different files. Place these files in a folder for a 13 – year old

# Creating the function
def genratetables(n):
    table = ""
    # Print the tables method in each file
    for i in range (1,11):
        table += f"{n} X {i} = {n*i}\n"
        # Creating files for tabales
    with open(f"Chapter-09/Tables/table_{n}.txt", "w") as f:
            f.write(table)

# Calling the function for the opration
for i in range(2,21):
    genratetables(i)

