#!/usr/bin/python
#write code to remove duplicates from an unsorted linked list
#FOLLOW UP
#How would you solve this problem if a temporary buffer is not allowed?

from classes.LinkList import *
# 2->3->5->6->5->None
#pass by the value of the reference, binding
def remove_duplicates(linklist ):
	if linklist.head == None : return
	
	curr_node = linklist.head
	while curr_node.next != None:
		runner = curr_node
		while runner.next != None: #doenst need to check the last one, no dups
			if runner.next.value== curr_node.value:
				runner.next = runner.next.next #found dup, remove
			else:
				runner = runner.next
		curr_node = curr_node.next
		
	
			
			 

if __name__ == "__main__":
	linklist = randomLinkList(7, 1, 20)
	print "orginal linklist: ", linklist
	remove_duplicates(linklist)
	print "removed duplicates: ", linklist

	linklist2 = randomLinkList(8, 1, 30)
	print "orginal linklist2: ", linklist2
	remove_duplicates(linklist2)
	print "removed duplicates: ", linklist2


