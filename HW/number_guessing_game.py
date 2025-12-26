import random

def start_game():
    # 1. Setup the game
    secret_number = random.randint(1, 100)
    guess_history = []  # This is our Data Structure (List)
    found = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # 2. Game Loop
    while not found:
        try:
            user_guess = int(input("Enter your guess: "))
            
            # Record the guess in our list
            guess_history.append(user_guess)

            # 3. Check the guess
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You found it in {len(guess_history)} tries.")
                found = True
        
        except ValueError:
            print("Please enter a valid whole number.")

    # 4. Display the Data Structure
    print("\nGame Summary:")
    print(f"Your guesses were: {guess_history}")

if __name__ == "__main__":
    start_game()