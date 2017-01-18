#!/usr/bin/python
'''
Implement an algorithm to delete a node in the middle of a singly linked list. 
given only access to that node.
EXAMPLE:
Input: the node c from the linked list a->b->c->d->e
Result: nothing is retuned, but the new linked list looks like a->b->d=>e
'''
from classes.LinkList import *

def removeNode(node):
	if node.next != None:
		node.value = node.next.value
		node.next = node.next.next
	else:
		node = None
			

if __name__ == "__main__":
	linklist = randomLinkList(5, 0, 20)
	node = linklist.head.next.next
	print linklist
	removeNode(node)		
	print linklist
	

