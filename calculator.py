"""
Calculator project
Created on Day 1

A basic calculator capable of doing basic arithmetic operations.
Can continue expressions, and take a look at result history.
Totally user-friendly and handles errors cleanly.
"""

import os
import sys
os.environ["TERM"] = "xterm-256color"

# Variables
EventLoop = True
tokens = []
first_number = None
operation = None
second_number = None
result = None
last_result = None
flag = True
result_history = []

# Definitions

def calc_parse(arg):
    """Splits and parses a calculation"""

    global tokens, first_number, second_number, operation, flag, last_result
    flag = True

    try:
        tokens = arg.split()
        for i in range(len(tokens)):
            tokens[i] = tokens[i].strip()
        first_number = tokens[0]
        if first_number == "ans":
            first_number = last_result
            flag = False
        if flag:
            first_number = int(tokens[0])
        operation = tokens[1]
        second_number = int(tokens[2])
        return tokens
    except ValueError:
        if flag:
            print("Don't include letters, only numbers!")
    except IndexError:
        print("Not enough characters, make sure to include an operation, and two numbers.")

def calculate():
    global first_number, second_number, operation, result

    try:
        if operation == '+':
            result = first_number + second_number
        elif operation == '-':
            result = first_number - second_number
        elif operation == '*':
            result = first_number * second_number
        elif operation == '/':
            result = first_number // second_number

        result_history.append(result)
        return result
    except TypeError:
        print("You didn't have a previous answer to begin with!")


os.system('clear')
while EventLoop:
    print("Calculator\n")
    print(f"Last Result: {last_result}")
    calculation = input("> ")
    calc_parse(calculation)
    calculate()
    print(result)
    last_result = result
    result = 0
    command_center = input("\nPress [ENTER] to continue... ").lower()
    if command_center == 'rlist':
        print(f"Previous Results\n{result_history}")
        input('Enter to continue...')
    elif command_center == "quit":
        os.system('clear')
        switch = False
        break

    os.system('clear')

print("Goodbye!")
sys.exit()