import os
from art import logo

#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")

auction = {}

def find_max_bidder(auction):
  max_bid = 0 # Create a variable assigned with 0 to hold the max bidding price
  max_bidder = "" # Create a variable assigned with empty string to hold the person with max bidding price
  for name, bid_price in auction.items(): # Loop through the dictionary items
    if bid_price > max_bid: # Loops all through the bids until it finds the max bidder
      max_bid = bid_price # max bid will be set to the integer with the highest price
      max_bidder = name # max bidder will be set to the bidder with the highest bidding price
  print(f"The winner is {max_bidder} with a bid of ${max_bid}")
  
while True: # Loop until there are other bidders
  name = input("What is your name?: ")
  bid_price = int(input("What's your bid?: $")) # Change input to integer
  other_bidders = input("Are there any other bidders? Type 'y' for yes and 'n' for no: ").lower()
  auction[name] = bid_price # Save the name and bid price in the dictionary
  os.system('clear')
  if other_bidders == 'n': 
    find_max_bidder(auction) # Call the function with the dictionary as an argument
    break




  
