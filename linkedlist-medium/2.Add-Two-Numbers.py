#!/usr/bin/python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        DEBUG_FLAG = True
            
        head = ListNode(0)
        curr = head
        
        carry = 0
        
        while True:

            val1 = l1.val
            val2 = l2.val
            
            if DEBUG_FLAG == True:
                print("l1 Val = {}".format(val1)) 
                print("l2 Val = {}\n".format(val2)) 

            curr.val = val1 + val2 + carry
            carry = 0
            if curr.val >= 10:
                curr.val -= 10
                carry += 1
                
            if l1.next == None or l2.next == None:
                break
                
            curr.next = ListNode(0)    
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        
        return head
