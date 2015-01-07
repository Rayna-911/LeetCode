# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None or head.next == None:
            return None
            
        slow = quick = head
        
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                break
        
        if slow == quick:
            slow = head
            while slow.next:
                if slow == quick:
                    return slow
                else:
                    slow = slow.next
                    quick = quick.next
        return None
