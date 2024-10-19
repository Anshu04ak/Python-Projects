import numpy as np

def guess_number():
    number = np.random.randint(1,10)

    print("********** WELCOME TO THE NUMBER GUESSING GAME **********")
    print("I'm thinking of a number betwwen 1 to 10")

    max_attempts = 3
    attempts=0
    guess=None

    while attempts < max_attempts:
        try:
            guess = int(input("Enter a number : "))

        except ValueError:
            print ("Please enter a valid number")
            continue

        attempts += 1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number}.")
        
guess_number()