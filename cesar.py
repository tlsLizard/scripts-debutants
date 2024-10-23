#!/usr/bin/env python3

alphabet='abcdefghijklmnopqrstuvwxyz'
#key = 3
newMessage=''

message = input('Please enter a message')
key= int(input('Please enter the encryption key'))

for character in message:
      if character in alphabet:
          position = alphabet.find(character)
          newPosition = (position + key) % 26
          newCharacter = alphabet[newPosition]
          #print('The new character is:',newCharacter)
          newMessage += newCharacter
      else:
          newMessage += character
print('your new message is:',newMessage)
