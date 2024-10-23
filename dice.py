#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Simple dice game in Python
"""

from random import randint           
import sys                           

print("Welcome to the dice game!")
       

while True:   
    answer = input("Do you want to roll the dice? y/n or q to quit")
    if answer.lower() == 'q':                                                                                         
        print("You want to quit the game... See you soon!")
        break
    else:
        if answer.lower()=='y':
            number = randint(1,6)
            print(number)
            
sys.exit() 
