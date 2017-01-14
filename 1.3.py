#!/usr/bin/python
'''
Check Permutation:
Given two strings, write a method to decide if one is a permutation of the other.
'''

import sys

def are_strings_permutations(string_1, string_2):
    # Check if strings have same length
    if len(string_1) != len(string_2):
        print("Nah... These strings are not permutations of each other.")
        return False

    # Create two dictionaries of ascii codes as hash table
    ascii_char_dict_1 = dict((i, 0) for i in range(128))
    ascii_char_dict_2 = dict((i, 0) for i in range(128))

    for i in range(len(string_1)):
        c1 = string_1[i]
        c2 = string_2[i]
        ascii_char_dict_1[ord(c1)] += 1
        ascii_char_dict_2[ord(c2)] += 1

    if ascii_char_dict_1 != ascii_char_dict_1:
        print("Nah... These strings are not permutations of each other.")
        return False

    print("Yay, {0} is just a permutation of {1}!".format(string_1, string_2))
    return True


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python 1.3.py STRING1 STRING2")
    else:
        are_strings_permutations(sys.argv[1], sys.argv[2])


