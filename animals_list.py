#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Create and manipulate a list
"""

# Print a message
print("Program that creates and manipulates a list:")

# Let's create a list of animals
animals = ['dog', 'cat', 'bird', 'rabbit', 'fish']

# Let's add an animal to the list
animals.append('mouse')

# Let's display the list
print("The list of animals is:", animals)

# Let's remove an animal from the list
animals.remove('bird')

# Let's display the updated list
print("The new list of animals is:", animals)

# Let's sort the list in alphabetical order
animals.sort()

# Let's display the sorted list
print("The sorted list of animals is:", animals)

# Let's display the number of animals in the list
print("The number of animals in the list is:", len(animals))

# Let's display the first animal in the list
print("The first animal in the list is:", animals[0])

# Print a message
print("End of the program...")
