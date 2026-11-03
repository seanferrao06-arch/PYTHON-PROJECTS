import random
secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 10

print("Welcome to the Number Guessing Game!")
print("I have selected a secret number between 1 and 100.")

while attempts < max_attempts:
    guess = int(input("Enter your guess:"))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
else:
    print(f"Sorry, you've used all {max_attempts} attempts. The secret number was {secret_number}.")
