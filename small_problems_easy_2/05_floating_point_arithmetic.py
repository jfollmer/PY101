# PY101-109 Small Problems, Easy 2, Problem 5. "Floating Point
# Arithmetic":

"""Write a program that prompts the user for two positive numbers 
(floating-point), then prints the results of the following operations on 
those two numbers: addition, subtraction, product, quotient, floor 
quotient, remainder, and power. Do not worry about validating the input.

Examples:
==> Enter the first number:
3.141529
==> Enter the second number:
2.718282
==> 3.141529 + 2.718282 = 5.859811
==> 3.141529 - 2.718282 = 0.42324699999999993
==> 3.141529 * 2.718282 = 8.539561733178
==> 3.141529 / 2.718282 = 1.1557038600115808
==> 3.141529 // 2.718282 = 1.0
==> 3.141529 % 2.718282 = 0.42324699999999993
==> 3.141529 ** 2.718282 = 22.45792517468373
"""

def prompt(string):
    print(f"==> {string}")

def input_prompt(string):
    return input(f"==> {string}")

def calculate(num1, num2):
    prompt(f"{num1} + {num2} = {num1 + num2}")
    prompt(f"{num1} - {num2} = {num1 - num2}")
    prompt(f"{num1} * {num2} = {num1 * num2}")
    prompt(f"{num1} / {num2} = {num1 / num2}")
    prompt(f"{num1} // {num2} = {num1 // num2}")
    prompt(f"{num1} % {num2} = {num1 % num2}")
    prompt(f"{num1} ** {num2} = {num1**num2}")

number1 = float(input_prompt("Enter the first number:\n"))
number2 = float(input_prompt("Enter the second number:\n"))

calculate(number1, number2)

# Given solution structures it this way for easier maintenance:

def calculate(first, second, operator):
    match operator:
        case '+':  return first + second
        case '-':  return first - second
        case '*':  return first * second
        case '/':  return first / second
        case '//': return first // second
        case '%':  return first % second
        case '**': return first ** second

first_float = float(input("==> Enter the first number:\n"))
second_float = float(input("==> Enter the second number:\n"))
for operator in ['+', '-', '*', '/', '//', '%', '**']:
    operation = f"{first_float} {operator} {second_float}"
    result = calculate(first_float, second_float, operator)
    print(f"==> {operation} = {result}")