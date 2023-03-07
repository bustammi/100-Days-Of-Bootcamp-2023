############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
from art import logo
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

deal_card()

def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2: # wins if the user/cpu has total of 21 and two cards in the deck already
        return 0
    if 11 in cards and sum(cards) > 21: # If there is "ACE (A)" in the deck and the sum is already greater than 21
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, cpu_score):
    """Compares the final score of the user and computer and determines the winner"""
    if user_score == cpu_score:
        return "It's a Draw!"
    elif cpu_score == 0:
        return "You lose! The opponent has the blackjack!"
    elif user_score == 0:
        return "You win with a blackjack!"
    elif cpu_score > 21:
        return "The opponent went over. You win!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif user_score > cpu_score:
        return "You win!"
    else:
        return "You lose!"
     
def play_game():
    """
    Deals the initial cards and asks the user to continue with another card
    If the user chooses not to continue or his score is greater than 21, the game ends
    Otherwise, the CPU draws the cards until it reaches a score greater than 16 or a "BUST"
    """
    print(logo)
    user_cards = [] #initialized an empty list 
    cpu_cards = []
    for _ in range(2):
        user_cards.append(deal_card()) #appending the empty list with random values chosen from deal_card function
        cpu_cards.append(deal_card())

    is_game_end = False

    while not is_game_end:
        """Calculate the score for user and computer and break the loop if 'game over' condition holds"""
        user_score = calculate_score(user_cards)  
        cpu_score = calculate_score(cpu_cards)
        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"\tComputer's first card: {cpu_cards[0]}")

        if user_score == 0 or cpu_score == 0 or user_score > 21:
            is_game_end = True
        else:
            #Prompt the user if they want another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card()) # add another number in the card by calling the deal_card function
            else:
                is_game_end = True 

    """Computer needs to keep drawing cards until it has a score lesser than 17 """
    while cpu_score != 0 and cpu_score < 17:
        cpu_cards.append(deal_card())
        cpu_score = calculate_score(cpu_cards)
    print("\n ")
    print(f"\tYour final hand: {user_cards}, final score: {user_score}")
    print(f"\tComputer's final hand: {cpu_cards}, final score: {cpu_score}")
    print(compare(user_score, cpu_score))

#Prompt the user if they want to restart the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('clear')
    play_game()


        
