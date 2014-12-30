# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        tmp = dummy
        
        while tmp.next and tmp.next.next:
            p = tmp.next.next
            tmp.next.next = p.next
            p.next = tmp.next
            tmp.next = p
            tmp = tmp.next.next
        
        return dummy.next
        
