# Calculator
A simple calculator that performs basic arithmetic operations such as addition, subtraction, multiplication, division, exponentiation, modulo, and floor division.

## Usage
Run the program to start the calculator and follow the prompts to input the numbers and choose an operation. The program will then return the result of the calculation.

## Features
- Supports basic arithmetic operations: addition, subtraction, multiplication, division, exponentiation, modulo, and floor division.
- Continues to calculate with the result of the previous calculation if desired.
- Handles invalid input, such as non-numeric values for numbers or invalid symbols for operations.

## Requirements
- Python 3.x
- art library

## Code Structure
The code defines functions for each of the operations and stores them in a dictionary called `operations`. The `calculator` function takes the user's input, performs the calculation using the chosen operation, and returns the result.

If an error occurs, such as invalid input, a `ValueError` is raised and the program will prompt the user to enter valid input again by calling the `calculator` function again.
