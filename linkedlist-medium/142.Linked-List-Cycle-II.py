# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        if not head.next:
            return None
        
        p_slow = head
        p_fast = head
        
        while p_fast and p_fast.next:
            p_fast = p_fast.next.next
            p_slow = p_slow.next
            if p_fast == p_slow:
                break
            
        if p_fast == p_slow:
            p_slow = head
            while p_fast != p_slow:
                p_fast = p_fast.next
                p_slow = p_slow.next                
            return p_slow
        
        if p_fast == None or p_fast.next == None:
            return None
