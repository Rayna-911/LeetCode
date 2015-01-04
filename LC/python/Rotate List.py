# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head == None:
            return None
        if k == 0:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        tmp = dummy
        cnt = 0
        while tmp.next:
            tmp=tmp.next
            cnt += 1
        
        tmp.next = dummy.next
        
        step = cnt - (k%cnt)
        for i in range(step): #shift left step = k%cnt
            tmp=tmp.next
        head = tmp.next
        tmp.next = None
        
        return head
