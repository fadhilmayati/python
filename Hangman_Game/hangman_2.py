# This is a comment in Python
# Author: fadhilmayati
# Date: Februrary 1, 2023
# Purpose: This program is a hangman game

# The rest of the code goes here
# Version: 1.0


import random

def hangman():
    words = ["tiger", "superman", "sand" , "thor", "doraemon", "avenger", "water", "stream", "love"]
    word = random.choice(words)
    turns = 10
    guessed = set()
    word_status = ["_"] * len(word)

    while turns > 0:
        print(" ".join(word_status))
        print("Turns left: ", turns)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    word_status[i] = guess
            if "_" not in word_status:
                print("You win! The word was: ", word)
                break
        else:
            turns -= 1
            print("Incorrect.")
    
    if "_" in word_status:
        print("You lose! The word was: ", word)

name = input("Enter your name: ")
print("Welcome", name)
print("=====================")
print("Try to guess the word in less than 10 attempts.")
hangman()
