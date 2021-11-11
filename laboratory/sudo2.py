"""
Sudo2 is for Loomgild.py
"""
import time
from time import sleep

# Command Functions

def help():
    print("Hello!")
    print("Welcome to Loomgild, a script that imitates a command line.")
    print("This is one of the few commands that you can use.")
    print("We will now load the commands you can use..")
    print("\n")
    sleep(2.00)
    print("Sys commands: exit")
    print("Core commands: none")
    print("Utility commands: help")
    print("Misc commands: none")

def output():
    prompt1 = input("Please provide the input to output: ")
    print(prompt1)

def output_h():
    print("Description: A command that outputs the user's input.")
    print("Usage: output")
    print("Tags: input, interactive")