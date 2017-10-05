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
        
        carry = 0
        # Dummy Head是一个比较好的方法，对付clone链表类
        dummy_head = ListNode(0)
        l3 = dummy_head
        l3_prev =dummy_head
        
        # 只要有一个没有空，就要一直算下去
        while l1 or l2 or carry != 0:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
                
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
                
            l3_val = l1_val + l2_val + carry

            l3.next = ListNode(l3_val % 10)
            
            carry = l3_val // 10
 
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
            l3 = l3.next
            l3_prev = l3


        # Dummy头不要，所以是next           
        return dummy_head.next
