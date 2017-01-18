#!/usr/bin/python
'''
Implement a function to check if a linked list is a palindrome.
'''
#using extra data structure, save all the values in array, can check if it is palindrome
#using the find_kth_last_element function 
#

#using array iterative solution
from classes.LinkList import *
def is_palindrome_iter1(linklist):
	val_array = []
	curr = linklist.head
	while curr != None:
		val_array.append(curr.value)
		curr = curr.next
	
	length = len(val_array)
	for i in range(length/2):
		if val_array[i] != val_array[length - i -1]:
			return False
	return True

#Iterative solution. save half of the linklist using slow and fast runner
def is_palindrome_iter(linklist):
	val_array = []
	slow = linklist.head
	fast = linklist.head
	while fast != None and fast.next != None:
		val = slow.value
		val_array.append(val)
		slow = slow.next
		fast = fast.next.next

	#if it is the odd number, move the slow to the next one
	if fast != None:
		slow = slow.next

	while slow != None:
		val = val_array.pop()
		if slow.value != val:
			return False
		slow = slow.next

	return True

#Recursive solution
def is_palindrome_recu(linklist):
	length = length_of_linklist(linklist)
	current = linklist.head
	result = is_palindrome_recu_helper(current, length)
	return result[1]

def is_palindrome_recu_helper(current, length):
	if current == None:
		return [None, True]
	elif length == 1:
		return [current.next, True]
	elif length == 2:
		return [current.next.next, current.value == current.next.value]

	#result is a python list stores two variables
	result = is_palindrome_recu_helper(current.next, length - 2)

	if result[0] == None or (not result[1]):
		return result
	else:
		result[1] = current.value == result[0].value
		result[0] = result[0].next
		return result

def length_of_linklist(linklist):
	length = 0
	current = linklist.head
	while current != None:
		length += 1
		current = current.next

	return length


if __name__ == "__main__":
	for i in range(10):
		linklist = randomLinkList(3,3,5)
		print linklist, 'iter ', is_palindrome_iter(linklist)
		print linklist, 'recu ', is_palindrome_recu(linklist)
		print '\n'
