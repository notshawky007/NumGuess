
"""
Number Guessing Game
This script runs a number guessing game where the player tries to guess a randomly generated number
within a specified range and number of attempts. The player can choose between three difficulty levels:
Easy, Medium, and Hard, each with different ranges and attempts.
Functions:
  number_guessing_game(): Main function to run the number guessing game. It handles user input for
              player name, difficulty level, and guesses. It provides feedback on guesses
              and allows the player to replay the game.
Usage:
  Run the script and follow the prompts to play the game.
"""
import random

def number_guessing_game():
    # Personalized Welcome Message
    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}! Welcome to the Number Guessing Game!")
    print("Choose a difficulty level: ")
    print("1. Easy (1–10, 5 attempts)")
    print("2. Medium (1–20, 4 attempts)")
    print("3. Hard (1–50, 3 attempts)")

    # Select difficulty level
    difficulty = input("Enter 1, 2, or 3 for your difficulty level: ")
    if difficulty == "1":
        max_number = 10
        max_attempts = 5
    elif difficulty == "2":
        max_number = 20
        max_attempts = 4
    elif difficulty == "3":
        max_number = 50
        max_attempts = 3
    else:
        print("Invalid choice! Defaulting to Easy mode.")
        max_number = 10
        max_attempts = 5

    # Replay counter
    replay_count = 0

    while True:
        print(f"\nGuess the number between 1 and {max_number}. You have {max_attempts} attempts.")
        target_number = random.randint(1, max_number)
        attempts = 0
        previous_guess = None

        while attempts < max_attempts:
            try:
                guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))

                # Check if the guess is correct
                if guess == target_number:
                    print(f"🎉 Congratulations, {player_name}! You guessed the correct number!")
                    break
                else:
                    # Bonus for close guesses
                    if abs(guess - target_number) <= 2:
                        print("You're very close! Just a bit off.")

                    # Hotter/Colder feedback
                    if previous_guess is not None:
                        if abs(guess - target_number) < abs(previous_guess - target_number):
                            print("Hotter!")
                        else:
                            print("Colder!")
                    else:
                        print("Wrong guess. Try again!")

                    # Higher or lower hint
                    if guess < target_number:
                        print("Hint: The number is higher.")
                    elif guess > target_number:
                        print("Hint: The number is lower.")

                    # Update previous guess and attempts
                    previous_guess = guess
                    attempts += 1

            except ValueError:
                print("Please enter a valid number!")

        # Game over condition
        if attempts == max_attempts:
            print(f"Game Over! The correct number was {target_number}.")

        # Replay option
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay == "yes":
            replay_count += 1
            print(f"Restarting game... Replay count: {replay_count}")
        else:
            print(f"Thanks for playing, {player_name}! You played {replay_count + 1} time(s). Goodbye!")
            break

# Run the game
number_guessing_game()
