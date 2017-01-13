#!/usr/bin/python
'''
String Rotation:
Assume you have a method isSubstring which checks if one word is a
substring of another. Given two strings, s1 and s2, write code to check
if s2 is a rotation of s1 using only one call to isSubstring
(e.g., "waterbottle" is a rotation of "erbottlewat"

'''

import unittest

def is_substring(string, sub):
    return string.find(sub) != -1

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    return is_substring(s1+s1, s2)


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('tokyo', 'newyork', False),
        ('arashiarashi', 'arashi', False),
        ('arashi', 'arashiarashi', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = is_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
