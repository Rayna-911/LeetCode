# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 == None: return l2
        elif l2 == None: return l1
        
        dummy = ListNode(0)
        tmp = dummy
        flag = 0
        
        while l1 and l2:
            tmp.next = ListNode((l1.val+l2.val+flag) % 10)
            flag = (l1.val+l2.val+flag) / 10
            l1 = l1.next 
            l2 = l2.next
            tmp = tmp.next
        if l1:
            while l1:
                tmp.next = ListNode((l1.val+flag) % 10)
                flag = (l1.val+flag) / 10
                l1 = l1.next
                tmp = tmp.next
        if l2:
            while l2:
                tmp.next = ListNode((l2.val+flag) % 10)
                flag = (l2.val+flag) / 10
                l2 = l2.next 
                tmp = tmp.next
        if flag == 1:
            tmp.next = ListNode(1)
            
        return dummy.next
        
        
