#!/usr/bin/python
# -*- coding: UTF-8 -*-

# prompt = "if you tell us who you are, we can personalize the message you sess."
# prompt += "\nWhat is your first name?"

# name = raw_input(prompt)
# print ("\nHello, " + name + "!")

# def greet_user(username):
# 	print ("Hello " + username.title() + "!")

# greet_user('henry')

def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
	print("\nPlease tell me your name:")
	f_name = raw_input("First name:")
	if f_name == 'q':
		break

	l_name = raw_input("Last name:")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")