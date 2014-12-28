# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    
    # slow & quick pointer
    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
            
        slow = quick = head
        
        while quick and quick.next:
            slow=slow.next
            quick = quick.next.next
            if slow == quick:
                return True
        
        return False
