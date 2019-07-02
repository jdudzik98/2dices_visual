from random import randint

class Die():
   """Jeden rzut kością."""
   def __init__(self, num_sides = 6):
       """num sides to ile kość ma ścian"""
       self.num_sides = num_sides
   def roll(self):
       """rzut"""
       return randint(1, self.num_sides)
