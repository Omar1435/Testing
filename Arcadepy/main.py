from random import randint as r

print("""Welcome to Begginer Arcade! Choose The Game you'll be playing today. Type <games> for a list of games. Note: Some games are still getting worked on, if you have any questions or suggestions please contact the makers of this. A GUI may be added in the future

Creator(s): Omar A. and Angel V.
""")

while True:
  user_types = input("> ").lower()
  if user_types == "games":
    print("""
1 - Rock, paper, scissors
2 - Random number guesser
3 - Not Mario Kart (To be Improved)
4 - Mad libs Game 1 (Under Maintenance)
5 - Dice Rolling Simulator
6 - Hangman (Under Maintenance)
7 - Mad libs Game 2
8 - What's the word?
""")
  else:
    print("Invalid.")
  if user_types in ["1", "2", "3", "4", "5", "6", "7", "8"]:
    break

if user_types == "1":

  print("To quit game type <quit>")
  while True: 
    rock = 1
    paper = 2 
    scissors = 3
    computer_move = r(1, 3)
    player_move = input("What do you choose? (rock/paper/scissors): ").lower()
    if player_move == "rock" and computer_move == 2:
      print("Bot picked paper")
      print("You lose!")
    elif player_move == "paper" and computer_move == 2:
      print("Bot picked rock")
      print("You win!")
    elif player_move == "paper" and computer_move == 1:
      print("Bot picked rock")
      print("You win!")
    elif player_move == "scissors" and computer_move == 2:
      print("Bot picked paper")
      print("You win!")
    elif player_move == "rock" and computer_move == 3:
      print("Bot picked scissors")
      print("You win!")
    elif player_move == "paper" and computer_move == 3:
      print("Bot picked scissors")
      print("You lose!")
    elif player_move == "scissors" and computer_move == 1:
      print("Bot picked rock")
      print("You win!")
    elif player_move == "rock" and computer_move == 1:
      print("It's a tie!")
    elif player_move == "paper" and computer_move == 2:
      print("It's a tie!")
    elif player_move == "scissors" and computer_move == 3:
      ("It's a tie!")
    elif player_move == "quit":
      print("The game has ended")
      break
    else:
      print("INVALID.")



elif user_types == "2":
  secret_num = r(1, 100)
  guess_limit = 6
  guess_count = 0
  while guess_limit > guess_count:
    answer = int(input("Enter you guess: "))
    guess_count += 1
    if answer == secret_num:
      print("You win!")
      break
    elif answer < secret_num:
      print("Higher")
    elif answer > secret_num:
      print("Lower")
  else:
    print("You lost!")



elif user_types == "3":

  print("Type <help> for a list of commands")

  started = False
  stopped = False 
  
  while True:
    command = input("> ").lower()
    if command == "start":
      if started == True:
        print("The car is already started")
      else:
        started = True
        print("The car has started")
    elif command == "stop":
      if started == True:
        print("You car has stopped")
        started = False
      else:
        print("Your car is already stopped")
    elif command == "help":
      print("""
      start - starts the car 
      stop - stops the car
      quit - ends the game
      """)
    elif command == "quit":
      print("The game has ended")
      break
    else:
      print("INVAID INPUT")

elif user_types == "4":
  verb = input("Enter a verb: ")
  print(verb)
  print(f" What's up.... {verb}")



elif user_types == "5":

  print("""welcome to a useless game, the dice only rolls a number between 1-6. I'll add more to this game later.
  
  Type <quit> to end game
  """)

  sides_input = int(input("Enter the number of sides on your dice would you like to have?: "))

  while True:

    command = input("Would you like to roll the dice? (Yes/No): ").lower()
    
    if command == "yes":
      dice_roll = r(1, sides_input)
      print(f"You rolled a {dice_roll}!")
    elif command == "no":
      dice_roll = r(1, sides_input)
      print(f"To bad, I'm rollng anyway. You rolled a {dice_roll}!")
    elif command == "quit":
      print("The game has ended")
      break
    else:
      print("INVALID.")



elif user_types == "6":
  print("Sorry not working, refresh the page!")


elif user_types == "7":

  day = input("Enter the weather or mood of a day: ")
  what = input("Enter something/someone: ")
  find = input("Enter something you were looking for: ")
  officer_says = input("What did the school's officer say to him?: ")
  acction = input(f"How did the {what} reply?: ")


  print(
  f"""One day on a {day} day, at school there was a {what}. The {what} looked around but couldn't find {find}. The school's officer comes up to him and says {officer_says}. Then the {acction} walks away and never comes back."""
  )



elif user_types == "8":

  print("In order to win this game, you'll have to guess the secret word. You only get 3 hints and 3 chances before you lose or win...")

  chances = 0
  secret_word = "silly"

  third_hint = "You laughed at a joke"
  second_hint = "You like to listen to jokes"
  first_hint = "You made a joke"

  print("Hint:")
  print(first_hint)

  while chances < 3:
    chances += 1
    user_types = input("Your prediction: ").lower()

    if user_types == secret_word:
      print("You guessed right!")
      break
    elif chances == 3:
      print("Oof, you lost!")
    elif chances == 1:
      print("Hint:")
      print(third_hint)
    elif chances == 2:
      print("Hint:")
      print(second_hint)
    else:
      print("Wrong. Try agian!")




  



      





    