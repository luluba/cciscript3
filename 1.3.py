#!/usr/bin/python
#Given two strings, write a method to decide if one is a permutation of the other.

def is_perm(str1, str2):
	if len(str1) != len(str2): return False

	return sorted(str1) == sorted(str2)


def main():
	str1 = "abbcde"
	str2 = "bbdeca"

	str3 = "aabb"
	str4 = "abcd"

	print str1 , str2, is_perm(str1, str2)
	print str3,  str4, is_perm(str3, str4)

if __name__ == "__main__":
	main()
