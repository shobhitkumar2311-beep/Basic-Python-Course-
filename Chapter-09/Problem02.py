# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.


import random
# Creating the function
def game():
    print("You are playing the game...")
    score = random.randint(1,999)
    return score

# Calling the funtion
new_score =  game()
print(f"Your score: {new_score}")

# Step 2: Read the old Hi-score (if file exists and not empty)
try:
    with open ("Chapter-09/hiscore.txt") as f:
        old_score = f.read()
        if old_score.strip() == "":
            old_score = 0
        else:
            old_score = int (old_score)

except FileNotFoundError:
        old_score = 0   # If file doesn't exist, assume 0


# Step 3: Compare and update if new score is higher
if new_score > old_score:
    print("🎉 New Hi-score!", new_score)
    with open("Chapter-09/hiscore.txt", "w") as f:
        f.write(str(new_score))
else:
    print("Current Hi-score remains:", old_score)