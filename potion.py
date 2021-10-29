"""
**PLEASE READ README.MD FOR MORE**
Configuration:
- Comment the "sleep" functions if it's too slow for you by doing # in front of the line
"""

import time
from time import sleep
import random
import laboratory
from laboratory import sudo1

print("---")
print("DISCLAIMER: Most stuff are coming soon, so don't expect this to get finished.")
print("---\n")

print("🧪🧪🧪\n")
print("Welcome to Aldrich's Potion Lab!")
print("🧪🧪🧪\n")
sleep(2.00)

print("Today, we've got a special menu just for you!\n")

print(".")
sleep(2.00)
print("..")
sleep(2.00)
print("...")
sleep(2.00)

print("\nBut wait!")
sleep(1.00)

name = input("Before we do that, let's get your name on the list! What's your name? ")

print("Processing..\n")
sleep(1.00)

print(f"Great to meet you, {name}!")
sleep(0.50)
print("Now that we've got your name, let's see what potion you got!")

print(sudo1.random_potion_final1)
print("Those are some excellent potions!")

prompt_answer1 = input("Let's pick, what do you want to brew? (1, 2, 3)\n")

def prompt_answer_func():
    if prompt_answer1 == "1" or 1:
        print(f"Great, so you want to use {sudo1.random_potion_final1}")