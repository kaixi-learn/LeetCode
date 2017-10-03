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
        DEBUG_FLAG = 0
        
        if DEBUG_FLAG == 1:
            curr = head
            while True:
                print("Curreent = {}".format(curr.val))
                if curr.next == None:
                    break
                curr = curr.next        
        
        head_odd = head
        head_even = head.next

        even = head_even # Point to N2
        odd = head_odd # Point to N1

        while True:
            if DEBUG_FLAG == 1:
                print("Odd Pointer = {}".format(odd.val))
                print("Even Pointer = {}".format(even.val))
                           
            odd.next = even.next
            odd = odd.next

            # End up with Even Node
            # If End up with Odd Node, Even Pointer Doesn't Need to Jump
            # If End up with Even Node, Even Pointer Needs to Jump

            if odd.next != None: 
                even.next = odd.next
                even = even.next
            
            if even.next == None:
                odd.next = head_even
                even.next = None
                break   
                
            if odd.next == None:
                odd.next = head_even
                even.next = None
                break

                
        if DEBUG_FLAG == 1:
            curr = head
            while True:
                print("Curreent = {}".format(curr.val))
                if curr.next == None:
                    break
                curr = curr.next   
                
        return head

