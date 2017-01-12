#!/usr/bin/python
'''
Palindrome Permutation:
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)

'''

import sys

def is_string_palindrome_permutation(input_string):

    # Create two dictionaries of ascii codes as hash table
    ascii_char_dict = dict((i, 0) for i in range(128))

    for i in range(len(input_string)):
        c = input_string[i]
        ascii_char_dict[ord(c)] += 1

    # Count characters that have odd occurrence
    odd_count = 0
    for c in ascii_char_dict.keys():
        if ascii_char_dict[c] % 2 == 1:
            odd_count += 1
        if odd_count > 1:
            print("Nah, {0} is not a palindrome permutation".format(input_string))
            return False

    print("Yay, {0} is a palindrome permutation!".format(input_string))
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 1.4.new.py INPUT_STRING")
    else:
        is_string_palindrome_permutation(sys.argv[1])