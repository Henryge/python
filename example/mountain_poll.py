#!/usr/bin/python
# -*- coding: UTF-8 -*- 

responses = {}

polling_active = True

while polling_active:
	name = raw_input("\nWhat is your name?")
	response = raw_input("Which mountain would you like to climb someday?")

	responses[name] = response

	repeat = raw_input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")