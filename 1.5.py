#!/usr/bin/python

'''
String Compression:

Implement a method to perform basic string compression using the counts
of repeated characters.
For example: the string aabcccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string,
your method should return the original string.
You can assume the string has only upper and lower case letter(a-z)
'''

import sys

def compress_string(input_string):
	if len(input_string) <= 1:
		print(input_string)
		return input_string

	new_string = ""
	count = 1
	for i in range(0, len(input_string)-1):
		if input_string[i] == input_string[i+1]:
			count += 1
		else:
			new_string += input_string[i] + str(count)
			count = 1

		if i == len(input_string) - 2:
			new_string += input_string[-1] + str(count)
			break

	if len(new_string) > len(input_string):
		print(input_string)
		return input_string
	else:
		print(new_string)
		return new_string


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 1.5.py input_string")
    else:
        compress_string(sys.argv[1])
