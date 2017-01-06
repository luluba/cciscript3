#!/usr/bin/python
import sys

'''
Is Unique:
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data
structures?
'''


def string_has_unique_chars(input_string):
    # Create an dictionary of ascii codes as hash table
    ascii_char_dict = dict((i, 0) for i in range(128))

    for c in input_string:
        ascii_char_dict[ord(c)] += 1
        if ascii_char_dict[ord(c)] > 1:
            print "Nah...Duplicate characters found in string. "
            return False

    print "Yay! All characters in the string are unique."
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: python 1_1_new.py STRING"
    else:
        string_has_unique_chars(sys.argv[1])