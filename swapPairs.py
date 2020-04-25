# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Variables:
    head referance => 1, next{2, next {3, next {4, next{None} } } }
    dummy_node = 0, next{None}
    dummy_node.next = head
    0, next{ 1, next{ 2, next { 3, next { 4, next{None} } } } }
    cur_node = 0
    first-iteration:
        first_node = 1
        second_node = 2
        first_node.next = 3
        second_node.next = 1
        cur_node.next = 2
        cur_node = 1
    0, next{ 2, next{ 1, next { 3, next { 4, next{None} } } } }
                      ^ cur_node
    second-iteration:
        first_node = 3
        second_node = 4
        first_node.next = None
        second_node.next = 3
        cur_node.next = 4
        cur_node = None
    0, next{ 2, next{ 1, next { 4, next { 3, next{None} } } } }
                                                    ^ cur_node

"""

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        dummy_node.next = head
        cur_node = dummy_node
        while cur_node.next !=  None and cur_node.next.next != None:
            first_node = cur_node.next
            second_node = cur_node.next.next
            first_node.next = second_node.next
            second_node.next = first_node
            cur_node.next = second_node
            cur_node = cur_node.next.next
        return dummy_node.next
