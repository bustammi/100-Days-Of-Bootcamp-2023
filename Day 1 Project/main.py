#1. Create a greeting for your program.
user_name = input("Hi there! What is your name? ")
print("Welcome to Band Name Generator")

#2. Ask the user for the city that they grew up in.
user_city = input("Hey " + user_name + ", what city did you grow up in? ")

#3. Ask the user for the name of a pet.
user_pet_name = input("So " + user_name + ", what is the name of your pet? ")

#4. Combine the name of their city and pet and show them their band name.
band_name = user_city + " " + user_pet_name

#5. Make sure the input cursor shows on a new line:
print("Congratulations " + user_name + ", your band name is: " + band_name)



# Solution: https://replit.com/@appbrewery/band-name-generator-end