# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if head == None or head.next == None:
            return head
        
        node = []
        
        start = tmp = head
        
        for i in range(m-1):
            start = start.next
            tmp = tmp.next
            
        for i in range(n-m+1):
            node.append(start.val)
            start = start.next
            
        for i in range(n-m+1):
            tmp.val = node[-1-i]
            tmp = tmp.next
        
        return head
        
