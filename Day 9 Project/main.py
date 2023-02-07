import os
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")

auction = []

def blind_auction(name, bid):
  curr_auction = {} #Create an empty dictionary
  curr_auction["name"] = name # Create a key "name" with the value of data being passed in the input
  curr_auction["bid_price"] = int(bid) # Create a key "bid_price" with the value of data being passed in the input
  auction.append(curr_auction) #Append the information together
  print(curr_auction)

  
while True: # Loop until there are other bidders
  name = input("What is your name?: ")
  bid_price = input("What's your bid?: $")
  other_bidders = input("Are there any other bidders? Type 'y' for yes and 'n' for no: ").lower()
  blind_auction(name, bid_price) #call the blind auction function to save inputs into a dictionary
  os.system('clear')
  if other_bidders == 'n': 
    break

max_bid = 0 #Create a variable assigned with empty value to hold the max bidding price
max_bidder = "" #Create a variable assigned with empty value to hold the person with max bidding price
for bid in auction: 
  if bid['bid_price'] > max_bid: #Loops all through the bids until it finds the max bidder
    max_bid = bid['bid_price'] #max bid will be set to the integer with the highest price
    max_bidder = bid['name'] #max bidder will be set to the bidder with the highest bidding price

print(f"The winner is {max_bidder} with a bid of ${max_bid}")


  
