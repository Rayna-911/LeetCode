# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head == None or k<=1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        
        while start.next:
            end = start
            for i in range(k-1):
                end = end.next
                if end.next == None:
                    return dummy.next
            r = self.reversePart(start.next,end.next)
            start.next = r[0]
            start = r[1]
        return dummy.next
        
        
    def reversePart(self,start,end):
        d = ListNode(0)
        d.next = start
        
        while d.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = d.next 
            d.next = tmp
        return [end,start]
        
