#!/usr/bin/python
'''
Implement a method to perform basic string compression using the counts of repeated characters. For example: the string aabcccccaaa would become a2b1c5a3. if the "compressed" string would not become smaller than the original string. your method should return the original string. You can assume the string has only upper and lower case letter(a-z)
'''

def compress(t_str):
	if len(t_str) == 0 or len(t_str) == 1: return t_str
	list = []
	count = 1
	for i in range(0, len(t_str)-1):
		if t_str[i] == t_str[i+1]:
			count += 1
		else:
			list.append(t_str[i])
			list.append(str(count))
			count = 1

		if i == len(t_str) - 2:
			list.append(t_str[-1])
			list.append(str(count))
	
	new_str = "".join(list)
	
	if len(new_str) > len(t_str):
		return t_str
	else:
		return new_str

def main():
	test = "aabcccccaaa"
	test1 = "aaccccccd"
	test2 = "abcde"
	print compress(test)
	print compress(test1)
	print compress(test2)

if __name__ == "__main__":
	main() 
