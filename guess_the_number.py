"""
Calculator project
Created on Day 1

A basic calculator capable of doing basic arithmetic operations.
Can continue expressions, and take a look at result history.
Totally user-friendly and handles errors cleanly.
"""

import os
import random
import time
import sys
os.environ["TERM"] = "xterm-256color"

# Definitions
def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


RESET = "\033[0m"
BOLD = "\033[1m"

# Variables
MainLoop = True
guesses = 0
EventLoop = True
chosen_number = None
switch = True


os.system('clear')
print(f"Guess the Number: Ultimate!\n")
start = input(f"Press {rgb(0, 255, 0)}[ENTER]{RESET} to start... ")
os.system('clear')



def level_setup(try_limit, level_name, min_range, max_range, message="Nice!"):
    global MainLoop, EventLoop, level, guesses, chosen_number, switch

    os.system('clear')
    placeholder = try_limit
    if try_limit == 'inf':
        placeholder = '∞'
    else:
        placeholder = try_limit
    print(f"{BOLD}Level:{RESET} {level_name}\n{BOLD}Allowed Tries:{RESET} {placeholder}\n{BOLD}Number Range:{RESET} {min_range} - {max_range}")
    input("Press [ENTER] to begin...")
    os.system('clear')
    chosen_number = str(random.randint(min_range, max_range))
    while MainLoop:
        if try_limit != 'inf':
            if guesses <= try_limit:
                if try_limit == 'inf':
                    print(f"{BOLD}Level:{RESET} {level_name}\n{BOLD}Guesses:{RESET} {guesses}\n{BOLD}Guesses Left:{RESET} ∞\nThe number is between {min_range} & {max_range}!\n")
                else:
                    print(f"{BOLD}Level:{RESET} {level_name}\n{BOLD}Guesses:{RESET} {guesses}\n{BOLD}Guesses Left:{RESET} {try_limit - guesses}\nThe number is between {min_range} & {max_range}!\n")
                guess = input("Guess a number >> ")
                if guess > chosen_number:
                    print("Too high!")
                    guesses += 1
                    input(f"Press {BOLD}[ENTER]{RESET} to try again...")
                    os.system('clear')
                elif guess < chosen_number:
                    print("Too low!")
                    guesses += 1
                    input(f"Press {BOLD}[ENTER]{RESET} to try again...")
                    os.system('clear')
                elif guess == chosen_number:
                    os.system('clear')
                    print(f"{message} You got it in {guesses} tries! The number was {chosen_number}")
                    input(f"Press {BOLD}[ENTER]{RESET} to continue...")
                    MainLoop = False
                    os.system('clear')
                elif guess.isalpha():
                    print("Only Numbers are allowed!")
                    input(f"Press {BOLD}[ENTER]{RESET} to try again...")
            else:
                print(f"You took too many tries! The number was: {chosen_number}")
                input(f"Press {BOLD}{rgb(255, 255, 255)}[ENTER]{RESET} to continue...")
                MainLoop = False
                os.system('clear')
        else:
            if try_limit == 'inf':
                print(
                    f"{BOLD}Level:{RESET} {level_name}\n{BOLD}Guesses:{RESET} {guesses}\n{BOLD}Guesses Left:{RESET} ∞\nThe number is between {min_range} & {max_range}!\n")
            else:
                print(
                    f"{BOLD}Level:{RESET} {level_name}\n{BOLD}Guesses:{RESET} {guesses}\n{BOLD}Guesses Left:{RESET} {try_limit - guesses}\nThe number is between {min_range} & {max_range}!\n")
            guess = input("Guess a number >> ")
            if guess > chosen_number:
                print("Too high!")
                guesses += 1
                input(f"Press {BOLD}[ENTER]{RESET} to try again...")
                os.system('clear')
            elif guess < chosen_number:
                print("Too low!")
                guesses += 1
                input(f"Press {BOLD}[ENTER]{RESET} to try again...")
                os.system('clear')
            elif guess == chosen_number:
                os.system('clear')
                print(f"{message} You got it in {guesses} tries! The number was {chosen_number}")
                input(f"Press {BOLD}[ENTER]{RESET} to continue...")
                MainLoop = False
                os.system('clear')
            elif guess.isalpha():
                print("Only Numbers are allowed!")
                input(f"Press {BOLD}[ENTER]{RESET} to try again...")
def game():
    global MainLoop, EventLoop, level, guesses, chosen_number, switch
    os.system('clear')
    MainLoop = True
    guesses = 0
    EventLoop = True
    chosen_number = None
    switch = True
    while EventLoop:
        print("Select Difficulty:")
        print(f"[1] {rgb(255, 255, 255)}Easy{RESET}\n[2] {rgb(169, 240, 98)}Normal{RESET}\n[3] {rgb(255, 162, 0)}Hard{RESET}\n[4] {rgb(219, 42, 42)}Insane{RESET}\n[5] {rgb(179, 92, 255)}IMPOSSIBLE{RESET}\n")
        level_select = input("Select a level number >> ").strip()
        if level_select == '1':
            print("Selected [EASY] level!")
            input(f"Press {BOLD}{rgb(255, 255, 255)}[ENTER]{RESET} to continue")
            level_setup('inf', 'Easy', 0, 8)
            EventLoop = False

        elif level_select == '2':
            print("Selected [NORMAL] level!")
            input(f"Press {BOLD}{rgb(255, 255, 255)}[ENTER]{RESET} to continue")
            level_setup(20, 'Normal', 0, 50)
            EventLoop = False

        elif level_select == '3':
            print("Selected [HARD] level!")
            input(f"Press {BOLD}{rgb(255, 255, 255)}[ENTER]{RESET} to continue")
            level_setup(10, 'Hard', 0, 80, "Getting better, eh?")
            EventLoop = False
        elif level_select == '4':
            print("Selected [INSANE] level.")
            input(f"Press {BOLD}{rgb(255, 255, 255)}[ENTER]{RESET} to continue")
            level_setup(7, 'Insane', 0, 140, "I wasn't sure you could do this one, but great!")
            EventLoop = False

        elif level_select == '5':
            print("Selected [IMPOSSIBLE] level, be prepared...")
            input(f"Press {BOLD}{rgb(255, 255, 255)}[ENTER]{RESET} to continue")
            level_setup(4, f'{BOLD}{rgb(150, 5, 5)}IMPOSSIBLE{RESET}', 0, 200, 'IMPOSSIBLE! How\'d you do it?')
            EventLoop = False

        else:
            print("That wasn't a level...")
            input(f"Press {BOLD}{rgb(255, 255, 255)}[ENTER]{RESET} to continue")
    while switch:
        play_again = input(f"Would you like to play again? {BOLD}[Y/n]{RESET}: ").lower().strip()
        if play_again == 'y':
            switch = False
            print("Restarting game...")
            game()
        elif play_again == 'n':
            switch = False
            os.system('clear')
            print("Goodbye!")
            sys.exit()
        else:
            print("Typo: There might've been a typo in your option, try again!")


if start == 'quit':
    os.system('clear')
    print("Goodbye!")
    sys.exit(101)
else:
    game()
