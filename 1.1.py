#!/usr/bin/python
#Implement an algorithm to determine if a string has all unique characters. What if you cannot use additonal data strucutere

def is_uniq_str(str):
	flag = {}
	for s in str:
		if s in flag:
			return False
		else:
			flag[s] = 1
	
	return True 

def is_uniq_str2(str):
	for i in range(len(str)-1):
		for j in range(i+1, len(str)):
			if str[i] == str[j]:
				return False
	
	return True
			
				

def main():
	test_str = "aabbcc"
	print is_uniq_str(test_str)
	print is_uniq_str2(test_str), '\n'

	test_str2 = "abcdef"
	print is_uniq_str(test_str2)
	print is_uniq_str2(test_str2), '\n'

	test_str3 = ""
	print is_uniq_str(test_str3)
	print is_uniq_str2(test_str3)

if __name__== "__main__":
	main()
