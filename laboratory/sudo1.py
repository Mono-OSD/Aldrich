import random

"""
Sudo1 is for Potion.py
"""

# Potion.py
list_of_potions1 = [
    'Potion of Swiftness', 'Potion of Harming', 'Potion of Healing',
    ''
]
list_of_potions2 = [
    'Potion of Acid'
]
list_of_potions3 = [
    ''
]

random_potion1 = random.choice(list_of_potions1)
random_potion2 = random.choice(list_of_potions2)
random_potion3 = random.choice(list_of_potions3)

random_potion_final1 = (random_potion1, random_potion2, random_potion3)