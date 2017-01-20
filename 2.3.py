#!/usr/bin/python3

'''
Delete Middle Node:
Implement an algorithm to delete a node in the middle (i,e,. any node but the first and last node,
not necessarily the exact middle) of a singly linked list,  given only access to that node.
EXAMPLE:
Input: the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
'''

from LinkedList import LinkedList

def delete_middle_node(ll, node):
    middle_node.next = middle_node.next.next
    middle_node.value = middle_node.next.value


ll = LinkedList()
ll.add_multiple([1, 2, 3, 4])
middle_node = ll.add(5)
ll.add_multiple([7, 8, 9])

print(ll)
delete_middle_node(ll, middle_node)
print(ll)