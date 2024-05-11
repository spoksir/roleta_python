
black_numbers = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]
red_numbers = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]

def is_valid_choice(choice):
  if choice in ["red", "black"]:
      return True
  try:
      num = int(choice)
      if 0 <= num <= 36:
       return True
  except ValueError:
        pass
  return False

def ask_for_choice():
  while True:
    choice = input("Try a number from 0 to 36 or 'red' or 'black': ")
    if is_valid_choice(choice):
      return choice
    else:
      print(f"The choice {choice} is not valid.")
      return None
    
def spin_roulette_wheel():
  import random
  return random.randint(0,36)

def get_roulette_wheel_outcome():
    numb_spin = spin_roulette_wheel()
    if numb_spin in red_numbers:
        return numb_spin, "red"
    elif numb_spin in black_numbers:
        return numb_spin, "black"
    else:
        return numb_spin, "green"


def ask_for_choice_until_valid():
    while True:
     choice = input("Try a number from 0 to 36 or red or black: ")
     if is_valid_choice(choice):
        return choice
     else:
        print(f"The choice {choice} is not valid.")

def ask_for_bet_until_valid(current_balance): 
    while True:
      try:
        bet_amount = int(input(f"What is your bet amount? Please enter a whole number (integer) between 0 and {current_balance}: "))
        if bet_amount < 0 or bet_amount > current_balance:
                    print(f"Invalid bet amount, Please enter a whole number (integer) between 0 and {current_balance}: ")
        else:
            return bet_amount
      except ValueError:
        print("Invalid input. Please enter a whole number: ")  

def main():
        
    #starting the game
        print("Welcome to the roulette game!")

balance = int(input("Please enter your initial balance (how much money they want to start with): "))

    # start the game loop
while True: # each iteration is a new round in the game (to be stopped if the player wants to, or runs out of money - balance is 0)

        # ask the player how much they want to bet, and save it
        bet_amount = ask_for_bet_until_valid(balance)
        # ✍️ TODO: discount the bet amount from the player's balance
        
        # ask for player's choice, and save it
        choice = ask_for_choice_until_valid()

        # get the number and color out of the roulette wheel spin
        number_outcome, color_outcome = get_roulette_wheel_outcome()

        # ✍️ TODO: check whether the player's choice matched the outcome (printing messages accordingly, with the outcome),
        if choice.isdigit():
            choice = int(choice)
            if choice == number_outcome:
                print(f" -> The roulette result is: {number_outcome}, {color_outcome} ")
                print("*******Congratulations! You're a winner!******* ")
                balance += bet_amount*35 
            else:
                print(f" -> The roulette result is: {number_outcome}, {color_outcome}")
                print("Sorry You loose!")
                balance -= bet_amount
        elif choice.lower() == "red" or choice.lower() == "black":
            if choice.lower() == color_outcome:
                print(f" -> The roulette result is: {number_outcome}, {color_outcome}")
                print("*******Congratulations! You're a winner!******* ")
                balance += bet_amount 
            else:
                print(f" -> The roulette result is: {number_outcome}, {color_outcome}")
                print("Sorry You loose!")
                balance -= bet_amount
        else:
                print("ERROR: Invalid choice. Try Again!")

    # ✍️ TODO: print the player's balance
                print(f" -> Your balance: {balance}")

    # ✍️ TODO: check whether the player's balance is 0, and if so, be sorry and break out of the game loop
        import time
        if balance == 0:
           print("Sorry, you've run out of money! You disconnect in 5 seconds...4....3....2....1...")
           time.sleep(5)
           break

    # ✍️ TODO: check whether the player wants to play again, and if not, say bye and break out of the game loop
        play_again = input("Do you want to keep playing? Write 'yes' continue or 'no' to cancel: ")
        if play_again.lower() != "yes":
            print("GoodBye!")
            print(f"You're balance is: {balance}!")
            print(f"Thanks for playing! You will disconnect in 5...4...3...2...1...")
            time.sleep(7)
            break
