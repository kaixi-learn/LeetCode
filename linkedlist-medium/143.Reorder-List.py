# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
            
        if not head:
            return None
        
        if not head.next:
            return None
        
        p_fast = head
        p_slow = head
        
        while p_fast and p_fast.next and p_fast.next.next:
            p_fast = p_fast.next.next
            p_slow = p_slow.next
            
        p_mid = p_slow.next
        p_slow.next = None 
        
        p_cur = p_mid
        p_prev = None
        
        while p_cur:
            p_next = p_cur.next
            p_cur.next = p_prev
            p_prev = p_cur
            p_cur = p_next

        
        p_cur_1 = head
        p_cur_2 = p_prev

        while p_cur_1 and p_cur_2:
            p_next_1 = p_cur_1.next
            p_next_2 = p_cur_2.next           
            p_cur_1.next = p_cur_2
            p_cur_1 = p_next_1
            p_cur_2.next = p_cur_1
            p_cur_2 = p_next_2

        return None        
            
            
            
