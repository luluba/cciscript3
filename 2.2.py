#!/usr/bin/python
'''
Implement an algorithm to find the kth to last element of a singly link list
'''
'''
have two runners, fast runner is k steps faster than the slow runner from the beginning, once the fast runner hits the end, whatever the slow runner is pointing to is the kth last element
'''


from classes.LinkList import *

def find_kth_last_element(linklist, k):
	count = 0 
	slow = linklist.head
	fast = linklist.head
	while fast != None and count < k:
		fast = fast.next
		count += 1
	
	if count == k and fast == None:
		return linklist.head.value

	if fast == None or count > k :
		return None

	while fast != None:
		slow = slow.next
		fast = fast.next

	return slow.value
# 7->2>3>4>1>9>2>5  3
		
if __name__ == "__main__":
	linklist = randomLinkList(9, 0, 15)
	print linklist
	print find_kth_last_element(linklist, 9)
