# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list = []
        l2_list = []

        # l1 压栈
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next


        # l2 压栈            
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next
            
        l3_list = []
        carry = 0
        
        # l1_list，l2_list 出栈，然后加法，再压栈到l3_list        
        while l1_list or l2_list or carry:
            if l1_list:
                l1_val = l1_list.pop() 
            else:
                l1_val = 0
            
            if l2_list:               
                l2_val = l2_list.pop()
            else:
                l2_val = 0
                
            l3_val = l1_val + l2_val + carry
            l3_list.append(l3_val % 10)
            carry = l3_val//10
       
        # l3_list出栈，然后再生成l3 linkedlist
        DummyHead = ListNode(0)
        l3 = DummyHead
        while l3_list:
            l3.next = ListNode(l3_list.pop())
            l3 = l3.next
        
        return DummyHead.next

