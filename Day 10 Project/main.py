#Calculator
from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

#Exponentiation
def power(n1, n2):
  return n1 ** n2

#Modulo
def modulo(n1, n2):
  return n1 % n2

#Floor Division
def floor_division(n1, n2):
  return n1 // n2

#Store functions inside a dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "**": power,
  "%": modulo,
  "//": floor_division
}

def calculator():
  print(logo)
  try:
    num1 = float(input("What is the first number? : "))
    for symbol in operations:
      print(symbol)
    calc_again = True

    while calc_again:
      operation_symbol = input("Pick an operation from the line above: ")
      if operation_symbol not in operations:
        raise ValueError("Invalid operation symbol")
      num2 = float(input("What is the second number?: "))
      calc_function = operations[operation_symbol] #assigns the value with the chosen key in dictionary
      answer = calc_function(num1, num2) #executes the operation with corresponding key
      print(f"{num1} {operation_symbol} {num2} = {answer}")

      calc_again_prompt = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower()
      if calc_again_prompt == "y":
        num1 = answer
      else: # if conditions are met
        calc_again = False # required condition
  except ValueError as ve:
    print("Invalid number entered. Please enter a valid number.")
    calculator() # Call the calculator again to prompt the user for input again

calculator()
