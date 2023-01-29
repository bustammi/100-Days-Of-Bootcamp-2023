import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_art = [rock, paper, scissors] # store the ascii art in a list so it can be recalled

# rock = 0
# paper = 1
# scissors = 2

while True:
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors. "))
  if user_choice < 0 or user_choice >= 3: 
    print("You provided an invalid input. Game Over!")
    break
  user_art = game_art[user_choice]# extracts the user choice and the ascii art
  ai_choice = random.randint(0, 2)# ai choice is randomly generated
  ai_art = game_art[ai_choice]# extracts the ai choice and ascii art
  
  if user_choice == ai_choice: # scenario where user and ai game is a draw
    print(f"You chose: {user_art} \n Computer chose: {ai_art} \n It's a draw.")
  elif (user_choice == 0 and ai_choice == 2) or (user_choice == 2 and ai_choice == 1) or (user_choice == 1 and ai_choice == 0): # all the scenarios where user beats ai (rock vs. scissors), (scissors vs. paper), (paper vs. rock)
    print(f"You chose: {user_art} \n Computer chose: {ai_art} \n You win! Congratulations")
  else:
    print(f"You chose: {user_art} \n Computer chose: {ai_art} \n You lose! Game over.")
    
  play_again = input("Would you like to try again? Type 'Y' for Yes or 'N' for No. ") # prompts the user to play again if they inputted "Y"
  if play_again.upper() == 'N': #breaks the while loop if the user chooses not to play again
    break
