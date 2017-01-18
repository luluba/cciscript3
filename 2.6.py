#!/usr/bin/python
'''
Given a circular linked list, implement an algorithm which returns the node at the beginning of the loop.
DEFINITION
Circular linked list: A(corrupt) linked list in which a node's next pointer points to an earlier node. so as to make a loop in the linked list.
EXAMPLE
Input: A->B->C->D->E->C
Output: C
'''

#using the slow and fast runner technique, find out the collision point which is LOOP_SIZE - k step away from the begining of the loop, and then move the slow point to the begining of the linklist, both slow and fast runner are moving one step each time, once they meet again, that is the begining of the loop.

from classes.LinkList import *
def find_entry(linklist):
	slow = linklist.head
	fast = linklist.head

	while fast != None and fast.next != None:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			break

	# it is not circular linklist
	if fast == None or fast.next == None:
		return None
	
	#move the slow runner to the begining of the linklist
	slow = linklist.head
	while slow != fast:
		slow = slow.next
		fast = fast.next

	return slow.value

def main():
	nodes_number = 100
	nodes_in_loop = 20
	linklist = LinkList()
	current = linklist.head
	store = []

	#create a linklist
	for i in range(nodes_number):
		linklist.addNode(i)
		current = linklist.head if i==0 else current.next
		store.append(current)

	#create loop
	current.next = None if nodes_in_loop <=0 else store[nodes_number - nodes_in_loop]
	print 'begining of the loop is ', find_entry(linklist)
	

if __name__ == "__main__":
	main()	
