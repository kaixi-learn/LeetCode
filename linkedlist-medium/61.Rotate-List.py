# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if not head:
            return None
        
        if k == 0:
            return head
        
        if not head.next:
            return head
        
        p_cur = head
        
        length = 0
        while p_cur:
            length += 1
            p_cur = p_cur.next
        
        
        p_prev = head
        p_cur = head
        
        i = k % length
        if i == 0:
            return head
        
        while i != 0:
            p_cur = p_cur.next
            if not p_cur:
                return head
            i -= 1
        
        while p_cur.next:
            p_prev = p_prev.next
            p_cur = p_cur.next
        
        p_new_head = p_prev.next
        p_prev.next = p_cur.next
        p_cur.next = head
       
        return p_new_head
            
            
