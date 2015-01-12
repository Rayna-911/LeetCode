# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head== None:
            return None
        tmp = head
        
        while(tmp):
            p = RandomListNode(tmp.label)
            p.next = tmp.next
            tmp.next =p
            tmp = tmp.next.next
            
        tmp = head
        while tmp:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next
        
        newhead = head.next
        old = head
        new = newhead
        while new.next:
            old.next = new.next
            old = old. next
            new.next = old.next
            new = new.next
        old.next = None
        new.next = None
        return newhead
            
