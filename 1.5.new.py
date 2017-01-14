#!/usr/bin/python
'''
One Away:
There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given tow strings, write a function to check if they are one edit
(or zero edits) away.

EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

'''

def is_remove(str1, str2):
	if len(str1) - len(str2) != 1: return False

	for i in range(len(str2)):
		if str1[i] == str2[i]:
			continue
		if str1[i+1] != str2[i]
			return False

		return True 

#pal, pael
def is_insert(str1, str2):
	if len(str2) - len(str1) != 1: return False
	
	for i in range(len(str1)):
		if str1[i] == str2[i]:
			continue
		if str1[i] != str2[i+1]
			return False

	return True	
		
def is_replace(str1, str2):
	if len(str1) != len(str2): return False
	count = 0

	for i in range(len(str1)):
		if str1[i] != str2[i]:
			count != 1


	if count != 1: return False
	else: return False	


def 
 
