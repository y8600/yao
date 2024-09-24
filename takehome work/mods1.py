#Directions: Create a hangman game
import random
# Use a list of words to choose from
word= "fat panda"
letters_Guessed= ""
#guess a single letter
failure_num=6
while failure_num> 0:
    guess= input("Please enter one letter ")
#track letters
    if guess in word:
        print(f"Great job, There is one or more letters in the secret word.")
#tries remaining    
    else:
        failure_num -=1
        print(f"your wonrg, there is no {guess} in this word, {failure_num} turns left!")

    letters_Guessed = letters_Guessed+ guess
    wrongLetter_num= 0
#user wins or loses
    for letter in word:
        if letter in letters_Guessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrongLetter_num+= 1

    if wrongLetter_num == 0:
        print(f" Congratulations! the secert word is {word}! ")
        break
else:
    print("Sorry you didn't win this game, please try again!")










