#!/usr/bin/python
# -*- coding: UTF-8 -*-

prompt = "\nTell me something, and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end program."

active = True
while active:
	message = raw_input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)
