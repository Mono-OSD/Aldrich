"""
Some parts are commented just for testing purposes.
On post-production, these comments will be removed or reduced.

By parts, I mean the sleep() functions.
"""
import time
from time import sleep
import random
import laboratory
from laboratory import sudo2
import sys

print("Welcome!")
print("Loomgild is a project that tries to imitate a command-line!")
print("Please wait for it to initialise..")

#sleep(2.00)

print("---")
sleep(0.50)
print("---")
sleep(0.50)
print("---")
sleep(0.50)

print("Starting initialising process.. (1/3)")
#sleep(4.0)
print("Installing necessary modules.. (2/3)")
#sleep(7.0)
print("Downloading necessary packages.. (3/3)")
print("- Package 1: SudoLabo (:: Downloading)")
#sleep(6.9)
print("- SudoLabo (:: Installing..)")
#sleep(22.0)
print("- SudoLabo (:: Cleaning things up..)")
#sleep(17.0)
print("Rebooting..")
#sleep(6.0)

print("Loomgild is a project that tries to imitate a command-line!")
print("Type in the command line to get started!")

cmd = input("> ")

while cmd == len(cmd)==2 or 3:
    cmd = input("> ")

    if cmd == "help":
        sudo2.help()
    if cmd == "exit":
        sys.exit()
    if cmd == "output":
        sudo2.output()
    elif cmd == "output -h":
        sudo2.output_h()
    else:
        print("That's not a valid command! If you need commands, please use \"help\"!")