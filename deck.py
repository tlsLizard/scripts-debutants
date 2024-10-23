#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Card deck
    Discovery of lists, tuples, nesting
"""

# On définit les couleurs, les niveaux
colors =  ["♥", "♦", "♣", "♠"]
#colors = ['hearts','clubs','diamond','spades']
levels = [i for i in range(1,14)]

# On initialise la liste deck
deck = []

# code de test
print (colors)
print ('Levels: ' + str(levels))


# On crée les cartes et on les append à deck
for level in levels:
    for color in colors:
        deck.append((level , color))
                      
# On affiche le deck                   
print(str(deck))

