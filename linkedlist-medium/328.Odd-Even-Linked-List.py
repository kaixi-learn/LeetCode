# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p_odd = ListNode(-1)
        p_odd_dummyhead = p_odd

        p_even = ListNode(-2)
        p_even_dummyhead = p_even
        cur = head
        i = 1
        while cur:
            if i % 2 == 1:
                p_odd.next = cur
                p_odd = p_odd.next
            if i % 2 == 0:
                p_even.next = cur
                p_even = p_even.next
            i += 1
            cur = cur.next
            
        p_even.next = None
        p_odd.next = p_even_dummyhead.next
        
        return p_odd_dummyhead.next
