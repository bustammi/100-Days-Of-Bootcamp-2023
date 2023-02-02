#Step 5

import random
import hangman_art as h_art
import hangman_words as h_word

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py 
chosen_word = random.choice(h_word.word_list) #randomly selects a word from the module "hangman_words.py"
word_length = len(chosen_word) 

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(h_art.logo) #hangman logo is printed from "hangman_art.py"
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

    
while not end_of_game: #loop until the 'end_of_game' variable is true
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display: #if the letter guessed is already in the blanks, then give feedback to user that they already inputted it.
        print(f"You already guessed the letter {guess}. You lost a life.")
        lives -=1 # user loses a life when condition above is true
      
    #Check guessed letter
    for position in range(word_length): #loops through each individual character in the `word_chosen` variable
        letter = chosen_word[position] # position is the current index of the word that the code is checking
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess: # code checks if the letter guessed is in the chosen word.
            display[position] = letter # If true, then the corresponding letter in the word is filled.

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        #The code now informs the user if the letter is not in the word
        lives -= 1
        print(f"The letter '{guess}' is not in the chosen word. You lost a life!")
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(h_art.game_over)
  

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(h_art.stages[lives])