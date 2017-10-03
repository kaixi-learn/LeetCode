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
        DEBUG_FLAG = True
        head_next = head.next
        odd_p = head
        even_p = head_next
        prev_p = even_p
        
        while True:

            if even_p.next != None:
                if prev_p != even_p:
                    prev_p.next = even_p
                odd_p.next = even_p.next
                even_p.next = odd_p
                even_p = odd_p.next.next
                prev_p = odd_p
                odd_p = odd_p.next
                
            if even_p.next == None:
                if prev_p != even_p:
                    prev_p.next = even_p               
                even_p.next = odd_p
                odd_p.next = None
                break
                
        if DEBUG_FLAG == True:
            curr = head_next
            while True:
                print("Curr = {}".format(curr.val))
                if curr.next == None:
                    break
                curr = curr.next    

        return head_next  
