 #!/usr/bin/python

'''
URLify:

Write a method to replace all spaces in a input_string with '%20'.
You may assume that the input_string has sufficient space at the end of the input_string
to hold the additional characters, and that you are given the "true" length of the input_string

EXAMPLE
Input: "Mr John Smith   ", 13
Output: "Mr%20John%20Smith"

'''

def urlify(input_string, length):
    all_length = len(input_string)

    for i in reversed(range(length)):
        if input_string[i] == ' ':
            if input_string[i-1] != ' ':
                continue
            else:

