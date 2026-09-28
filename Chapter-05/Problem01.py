# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
 # step 1 
Dictionary = {
    "Khana": "food",
    "Paani": "water",
    "Ghar": "home",
    "Dost": "friend",
    "Rasta": "road"
    }
word = input("Enter a Hindi word to look up its English translation: ")
translation = Dictionary.get(word)
if translation:
    print("The English translation is: ",translation)
else:
    print("The Word is not found in the dicitionary")
