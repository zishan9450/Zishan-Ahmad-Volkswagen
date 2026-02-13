# 3. Number Guessing Game
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 7 attempts to guess it.")

secret_number = random.randint(1, 100)
max_attempts = 7
attempts = 0

while attempts < max_attempts:
    attempts += 1
    guess = int(input(f"\nAttempt {attempts}/{max_attempts} - Enter your guess: "))
    
    if guess == secret_number:
        print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
        break
    elif guess > secret_number:
        print("Too high! Try a smaller number.")
    else:
        print("Too low! Try a larger number.")
else:
    print(f"\nGame Over! You've used all {max_attempts} attempts.")
    print(f"The correct number was {secret_number}.")
