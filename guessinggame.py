import random

def guess_game():
  # Generate a random number between 1 and 100
  secret_number = random.randint(1, 100)
  guess_count = 0

  # Welcome message
  print("Welcome to the guessing game!")

  # Main game loop
  while True:
    try:
      # Get user guess
      guess = int(input("Guess a number between 1 and 100: "))
      guess_count += 1

      # Check for win/loss
      if guess == secret_number:
        print(f"You guessed it! The number was {secret_number} in {guess_count} tries.")
        break
      elif guess < secret_number:
        print("Too low, try again!")
      else:
        print("Too high, try again!")
    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  guess_game()
