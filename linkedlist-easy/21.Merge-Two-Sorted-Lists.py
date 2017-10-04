# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        DEBUG_FLAG = True
        l1_cur = l1
        l2_cur = l2        
        if DEBUG_FLAG == True:
            while True:
                print("l1_cur = {}".format(l1_cur.val))
                if l1_cur.next == None:
                    break
                l1_cur = l1_cur.next
            print("\n")
            while True:
                print("l2_cur = {}".format(l2_cur.val))
                if l2_cur.next == None:
                    break
                l2_cur = l2_cur.next                     
        print("\n")
               
        l1_cur = l1
        l2_cur = l2
        l3_prehead = ListNode(0)
        l3_cur = l3_prehead

        while True:
            # Alway point the l3_cur to the small node
            if l1_cur.val <= l2_cur.val:
                l3_cur.next = l1_cur
                l1_cur = l1_cur.next
            else:
                l3_cur.next = l2_cur
                l2_cur = l2_cur.next
            l3_cur = l3_cur.next
            
            # Hit End of Node and Break
            if l1_cur == None or l2_cur == None:
                if l1_cur == None:
                    print("l1 is None, Attach L2 Nodes as the tail")
                    l3_cur.next = l2_cur
                if l2_cur == None:
                    print("l2 is None, Attach L1 Nodes as the tail")   
                    l3_cur.next = l1_cur
                break
        
            
        if DEBUG_FLAG == True:
            l3_cur = l3_prehead.next
            while True:
                print("l3_cur = {}".format(l3_cur.val))
                if l3_cur.next == None:
                    break
                l3_cur = l3_cur.next
                
        return l3_prehead.next

