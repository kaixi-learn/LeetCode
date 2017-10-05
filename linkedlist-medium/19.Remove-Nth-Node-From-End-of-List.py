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
        
        p_prev = head
        p_cur = p_prev
        
        i = n
        while i:
            p_cur = p_cur.next
            i -= 1
        
        if not p_cur:
            return head.next
        
        while p_cur.next:
            p_cur = p_cur.next
            p_prev = p_prev.next
        
        p_prev.next = p_prev.next.next
        
        return head
        
