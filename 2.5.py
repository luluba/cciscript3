#!/usr/bin/python
'''
You have two numbers represented by a linkedlist, where each mode contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a lined list.
EXAMPLE
Input:(7->1->6) + (5->9->2). That is 617 + 295
Output:2->-1->9. That is 912
FOLLOW UP
Suppose the digits are stored in the forward order. Repeat the above algorithm.
EXAMPLE
Input: (6->1->7) + (2->9->5). That is 617 + 295
Output: 9->1->2. That is 912.
'''
from classes.LinkList import *
def add_sum_link(linklist1, linklist2):
	sum = LinkList()
	curr1 = linklist1.head
	curr2 = linklist2.head
	rest = 0
	while curr1 != None and curr2 != None:
		val = ( rest + curr1.value + curr2.value) % 10
		rest = ( rest + curr1.value + curr2.value) / 10
		sum.addNode(val)
		curr1 = curr1.next
		curr2 = curr2.next	
		
	if curr1 == None and curr2 != None:
		while curr2 != None:
			val = (rest + curr2.value) % 10
			rest = (rest + curr2.value) / 10
			sum.addNode(val)
			curr2 = curr2.next

	if curr2 == None and curr1 != None:
		while curr1 != None:
			val = (rest + curr1.value) % 10
			rest = (rest + curr1.value) / 10
			sum.addNode(val)
			curr1 = curr1.next

	if rest > 0:
		sum.addNode(rest)
	print 'sum ', sum	

#solution from the book, neat
def add_sum_rev(linklist1, linklist2):
	sum = LinkList()
	curr1 = linklist1.head
	curr2 = linklist2.head
	carry = 0
	while curr1 != None or curr2 != None or carry != 0:
		val = carry
		if curr1 != None:
			val += curr1.value
			curr1= curr1.next
		if curr2 != None:
			val += curr2.value
			curr2 = curr2.next

		carry = val/10
		val = val%10
		sum.addNode(val)
	return sum

#For FOLLOWUP, the digits are stored in the forward order
#Iterative Implementation
def add_sum_fwd(linklist1, linklist2):
	#create two new linklists which are revesed version of l1, l2
	#and use the add_sum_rev method and then reverse the sum list
	l1_rev = reverse_LinkList(linklist1)
	l2_rev = reverse_LinkList(linklist2)

	sum = add_sum_rev(l1_rev, l2_rev)
	sum_fwd = reverse_LinkList(sum)
	return sum_fwd

#Recursive Implementation of add_sum_fwd
def add_sum_fwd2(linklist1, linklist2):
	#compare length of linked lists and pad the shorter one with 0
	l1_len = lengthOfLinkList(linklist1)
	l2_len = lengthOfLinkList(linklist2)
	if l1_len < l2_len:
		linklist1 = padInFront(linklist1, l2_len - l1_len)
	else:
		linklist2 = padInFront(linklist2, l1_len - l2_len)

	#Add lists
	sumandcarry = addListFwd2Helper(linklist1.head, linklist2.head)
	result = LinkList()
	result.head = sumandcarry[0]
	if sumandcarry[1] != 0:
		insertBefore(result, sumandcarry[1])
	return result

#the helper function of add sum fwd
def addListFwd2Helper(n1, n2):
	if n1 == None and n2 == None:
		sumandcarry = [None, 0]
		return sumandcarry

	sumandcarry = addListFwd2Helper(n1.next, n2.next)
	val = n1.value + n2.value + sumandcarry[1]
	head = addNodeInfront(sumandcarry[0], val/10)
	return [head, val/10]

#insert a Node infron the node and return the node
def addNodeInFront(node, val):
	new_node = Node(val)
	new_node.next = node
	return new_node

def lengthOfLinkList(linklist):
	count = 0
	curr = linklist.head
	while curr != None:
		count += 1
		curr = curr.next
	return count

def reverse_LinkList(linklist):
	if linklist.head == None: return linklist
	new_linklist = LinkList()
	new_linklist.head = Node(linklist.head.value)
	curr = linklist.head.next
	while curr != None:
		val = curr.value
		insertBefore(new_linklist, val)
		curr = curr.next

	return new_linklist

def insertBefore(linklist, val):
	node = Node(val)
	node.next = linklist.head
	linklist.head = node	
	

if __name__ == "__main__":
	linklist1 = randomLinkList(5, 1, 9)
	linklist2 = randomLinkList(5, 1, 9)
	print 'linklist1 ', linklist1
	print 'linklist2 ', linklist2
	add_sum_rev(linklist1, linklist2)	

	linklist1 = randomLinkList(4, 1, 9)
	linklist2 = randomLinkList(3, 1, 9)
	print 'linklist1 ', linklist1
	print 'linklist2 ', linklist2
	add_sum_rev(linklist1, linklist2)	

	linklist1 = randomLinkList(5, 1, 9)
	linklist2 = randomLinkList(6, 1, 9)
	print 'linklist1 ', linklist1
	print 'linklist2 ', linklist2
	add_sum_link(linklist1, linklist2)	

	linklist1 = randomLinkList(5, 1, 9)
	linklist2 = randomLinkList(6, 1, 9)
	print 'linklist1 ', linklist1
	print 'linklist2 ', linklist2
	print 'add sum fwd', add_sum_fwd(linklist1, linklist2)	

	linklist1 = randomLinkList(5, 1, 9)
	linklist2 = randomLinkList(6, 1, 9)
	print 'linklist1 ', linklist1
	print 'linklist2 ', linklist2
	print 'add sum fwd', add_sum_fwd2(linklist1, linklist2)	
