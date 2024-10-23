# -*- coding: utf-8 -*-

"""
Script découverte des dictionnaires
"""


# Dictionnaires

# deux méthodes pour créer un dictionnaire

tel = {'jack': 4098, 'sape': 4139}
print(tel)
tel['guido'] = 4127
print(tel)


#constructor
tel2 = dict(sape=4139, guido=4127, jack=4098)
print(tel2)



knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
    print(k, v)



