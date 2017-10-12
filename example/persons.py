#!/usr/bin/python
# -*- coding: UTF-8 -*- 

def build_person(first_name, last_name, age=''):
	person = {'first_name':first_name, 'last':last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)