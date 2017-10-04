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
        
        DEBUG_FLAG = True

        forward_p = head 
        behind_p = head
        for i in range(n):
            forward_p = forward_p.next
              
        if DEBUG_FLAG == True:
            print("forward_p = {}".format(forward_p.val))
            print("behind_p = {}".format(behind_p.val))

        while True:
            if forward_p.next == None:
                if n > 1:
                    behind_p.next = behind_p.next.next
                    break
                if n == 1:
                    behind_p.next = None 
                    break
            forward_p = forward_p.next
            behind_p = behind_p.next
        return head    

