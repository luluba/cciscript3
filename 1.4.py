#!/usr/bin/python
#Write a method to replace all spaces in a string with '%20'.
#You may assume that the string has sufficient space at the end of the string
#to hold the additional characters, and that you are gvin the "true" length of the string
#Input: "Mr John Smith   ", 13
#Output: "Mr%20John%20Smith"

def replace_with(str, length):
	rel_str = "%20"
	i = 0;
	new_str = [] 
	while i < length:
		if str[i] == " ":
			new_str.append(rel_str)
		else:
			new_str.append(str[i])
		i += 1
	return "".join(new_str)

def main():
	input = "Mr John Smith   "
	print replace_with(input, 13)

if __name__ == "__main__":
	main()
