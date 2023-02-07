import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  for letter in start_text:
    if letter not in alphabet:
      end_text += letter
    else:
      letter_idx = alphabet.index(letter)
      if cipher_direction == "encode":
        shift_idx = (letter_idx + shift_amount) % len(alphabet)
      else:
        shift_idx = (letter_idx - shift_amount) % len(alphabet)
      end_text += alphabet[shift_idx]
  print(f"Here's the {cipher_direction}d result: {end_text}")

print(art.logo)

while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  while direction != "encode" and direction != "decode":
    direction = input("Invalid input. Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n")) 
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  cipher_again = input("Do you want to restart the cipher program? Type 'yes' or 'no' ").lower()
  if cipher_again == "no":
    break

