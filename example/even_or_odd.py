#!/usr/bin/python
# -*- coding: UTF-8 -*-

number = raw_input("Enter a number, and I'll tell you if it's even or odd:")
print isinstance(number, basestring)

number = int(number)

if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")