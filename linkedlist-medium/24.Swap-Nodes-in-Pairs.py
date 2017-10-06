# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        dummy_head = ListNode(0)
        dummy_head.next = head
        p_prev = dummy_head
        p_1 = head
        p_2 = head.next
        
        while p_2:
            p_temp = p_2.next
            p_prev.next = p_2
            p_2.next = p_1
            p_1.next = p_temp
            
            if p_temp == None:
                break
            
            p_prev = p_1
            p_1 = p_temp
            p_2 = p_temp.next
        
        return dummy_head.next
