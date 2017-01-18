#!/usr/bin/python
'''
Write code to partition a linked list around a value x ,such that
all nodes less than x come before all nodes greater than or equal to x
'''
#6->3->4->6->7->5>8 , 5
#prev, curr
from classes.LinkList import *
def partition(linklist, val):
	beforeHead = None
	beforeTail = None
	afterHead  = None
	afterTail  = None

	curr = linklist.head
	while curr != None:
		next = curr.next
		curr.next = None #make sure each time append the node, it is always pointing to the None to terminate the link
		if curr.value < val:
			if beforeHead is None:
				beforeHead = curr
				beforeTail = curr
			else:
				beforeTail.next = curr
				beforeTail = curr
		else:
			if afterHead is  None:
				afterHead = curr
				afterTail = curr
			else:
				afterTail.next = curr
				afterTail = curr
		curr = next	
	beforeTail.next = afterHead
	
	linklist.head = beforeHead

if __name__ == "__main__":
	linklist = randomLinkList(5, 1, 10)
	print "original ", linklist
	partition(linklist, 8)
	print "after partition ", linklist	
	

