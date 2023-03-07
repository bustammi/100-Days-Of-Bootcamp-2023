# Blackjack Game

This is a simple command-line-based Blackjack game developed in Python.

## Rules

* The deck is unlimited in size
* There are no jokers
* The Jack/Queen/King all count as 10
* The Ace can count as 11 or 1
* Use the following list as the deck of cards: `cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
* The cards in the list have equal probability of being drawn
* Cards are not removed from the deck as they are drawn
* The computer is the dealer

## How to Play

1. Run the script in a Python environment.
2. The game will prompt you to start by typing 'y' or 'n' to exit.
3. The game will display your cards and the computer's first card.
4. You will be prompted to choose whether to draw another card or pass.
5. If your total score exceeds 21, you lose.
6. If the computer's total score exceeds 21, you win.
7. If you get a blackjack (an Ace and a card with a value of 10), you win.
8. If the computer gets a blackjack, you lose.
9. If you choose to pass or your total score is greater than the computer's total score, the computer will start drawing cards.
10. The game will end once both players have passed or one of them exceeds 21.

## Dependencies

This game uses the following Python libraries:

* `random`
* `os`
* `art`

## Documentation

For further documentation, please refer to the code comments and Python docstrings in the script.
