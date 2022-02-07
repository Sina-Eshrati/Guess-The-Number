from art import logo
import random
from replit import clear

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(1,100)
    print(number)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f" You got it! The answer was {number}")
            attempts = 0
        elif guess > number:
            print(" Too high!")
            attempts -= 1
        else:
            print(" Too low!")
            attempts -= 1
        if attempts > 0 and guess != number:
            print(" Guess again.")
    if guess != number:
        print("You've run out of guesses, you lost.")
    play_again = input("Do you want to play again? (Type 'y' or 'n') ")
    if play_again == 'y':
        clear()
        play_game()

play_game()