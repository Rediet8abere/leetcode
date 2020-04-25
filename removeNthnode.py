# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """
        Variable:   input 1->2->3->4->5 n=2
            dummy_node: 0
            dummy_node.next = 0->1->2->3->4->5
            first_iteration:
                cur_node = 0  cur_node = 1   cur_node = 2  cur_node = 3   cur_node = 4  cur_node = 5
                length = 0    length = 1     length = 2    length = 3     length = 4    length = 5
            second_iteration:
                pos=3
                cur_node=0  cur_node=1   cur_node=2  cur_node=3
                length=0    length=1     length=2    length=3

            delete = 4
            cur_node.next = 5
            delete.next = None

        """

        dummy_node = ListNode(0)
        dummy_node.next = head
        cur_node = dummy_node
        length = 0
        while cur_node.next != None:
            length += 1
            cur_node = cur_node.next

        pos = length - n
        length = 0
        cur_node = dummy_node
        while length != pos and cur_node != None:
            cur_node = cur_node.next
            length += 1
        delete = cur_node.next
        cur_node.next = cur_node.next.next
        delete.next = None
        return dummy_node.next
