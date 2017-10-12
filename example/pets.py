#!/usr/bin/python
# -*- coding: UTF-8 -*- 

# pets = ['dog', 'cat', 'dog', 'glodfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
# 	pets.remove('cat')

# print(pets)

def describe_pet(animal_type, pet_name):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')