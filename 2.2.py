#!/usr/bin/python3

'''
Return Kth to Last:
Implement an algorithm to find the kth to last element of a singly link list
'''

from LinkedList import LinkedList

def return_kth(ll, k):
    if ll.head is None:
        return None

    len_linked_list = 1
    pos = ll.head
    while pos.next:
        pos.next.prev = pos
        pos = pos.next
        len_linked_list += 1

    if k > len_linked_list:
        return None

    print("""Length of Linked List: {0}""".format(len_linked_list))
    # import pdb; pdb.set_trace()
    while k-1:
        pos = pos.prev
        k -= 1

    return pos

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(return_kth(ll, 3))
