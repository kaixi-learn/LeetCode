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
        DEBUG_FLAG = 1
    
        slow_pointer = head
        fast_pointer = head

        '''
        Check if there is a loop
        '''
        while fast_pointer and fast_pointer.next :
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                break 

        if fast_pointer == None:
            return None
        
        # Reset Slow Pointer. 
        slow_pointer = head
        while slow_pointer != fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next

        return slow_pointer
