#!/usr/bin/python
from random import randint
class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		return str(self.value)


class LinkList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def addNode(self, value):
		node = Node(value)
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node		
			self.tail = node
			
	#remove the first node that has the same value as the node_value
	def removeNode(self, node_value):
		current = self.head
		if current.value == node_value:
			self.head = self.head.next
#		7->3->2->1->2->1->None
		while current.next != None:
			if (current.next.value == node_value):
				current.next = current.next.next
				break;
			current = current.next

		#if the tail is the same value as the node_value, remove tail
		if current.value == node_value:
			current = None
				
	def __str__(self):
		if self.head != None:
			index = self.head
			nodestore = [str(index.value)]
			while index.next != None:
				index = index.next
				nodestore.append(str(index.value))
			return "Linklist [" + "->".join(nodestore) + "]"
		return "LinkList []"


def randomLinkList(length, min, max):
		linklist = LinkList()
		for i in range(length):
			value = randint(min, max)
			linklist.addNode(value)
		return linklist	


	
				
	
