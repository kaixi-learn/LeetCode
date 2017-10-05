class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        DEBUG_FLAG = True

        '''
            Dump Value from l1 and l2 to List(Stack) l1_list and l2_list
        '''

        l1_list = []
        l2_list = []


       # l1压stack
        while True:
            if DEBUG_FLAG == True:
                print("l1 Val = {}".format(l1.val))
            l1_list.append(l1.val)

            if l1.next == None :
                break
            l1 = l1.next

       # l2压stack
        while True:
            if DEBUG_FLAG == True:
                print("l2 Val = {}".format(l2.val))
            l2_list.append(l2.val)

            if l2.next == None :
                break
            l2 = l2.next

        if DEBUG_FLAG == True:
            print("l1_list = {}".format(l1_list))
            print("l2_list = {}".format(l2_list))

        i = 0
        carry = 0
        l3_list = []


        '''
            Extract from List(Stack) and Sum Them
        '''

        if DEBUG_FLAG == True:
                print("l1 length = {}".format(len(l1_list)))
                print("l2 length = {}".format(len(l2_list)))


       # l1, l2出stack
        while True:
            if len(l1_list) == 0:
                val1 = 0
            else:
                val1 = l1_list.pop()

            if len(l2_list) == 0:
                val2 = 0
            else:
                val2 = l2_list.pop()


            if DEBUG_FLAG == True:
                print("val1 = {}".format(val1))
                print("val2 = {}".format(val2))



       # l1, l2做加法，再stack
            val3 = val1 + val2 + carry
            carry = 0

            carry = val3 / 10
            val3 = val3 % 10

            l3_list.append(val3)

            if len(l1_list) == 0 and len(l2_list) == 0:
                break

        if DEBUG_FLAG == True:
            print("l3_list = {}".format(l3_list))

        '''
            Extract from New List (Stack) and Create a Linked List to Carry these Values
        '''
        head = ListNode(0)
        curr = head
        while True:
            val3 = l3_list.pop()
            if DEBUG_FLAG == True:
                print("val3 = {}".format(val3))
                print("l1_list Length = {}".format(len(l3_list)))
            curr.val = val3

            if len(l3_list) == 0:
                break

            curr.next = ListNode(0)
            curr = curr.next

        return head
