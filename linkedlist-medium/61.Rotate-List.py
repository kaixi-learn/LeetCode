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
        DEBUG_FLAG = True
        behind_p = head
        forward_p = head
        for i in range(k):
            forward_p = forward_p.next

        while True:
            if forward_p.next == None:
                forward_p.next = head
                head = behind_p.next
                behind_p.next = None
                break
            forward_p = forward_p.next
            behind_p = behind_p.next
        
        if DEBUG_FLAG == True:
            cur = head
            while True:
                print("Current = {}".format(cur.val))
                if cur.next == None:
                    break
                cur = cur.next
        
        return head

