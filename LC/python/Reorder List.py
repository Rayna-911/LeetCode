# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None or head.next == None:
            return head
        
        #slice list to two
        slow = head
        quick = head
        while quick.next and quick.next.next:
            slow = slow.next
            quick = quick.next.next
            
        head1 = head
        head2 = slow.next
        slow.next = None
        
        #reverse list2
        p1 = head2
        p2 = head2.next
        head2.next = None
        while p2:
            tmp = p2
            p2 = p2.next
            tmp.next = p1
            p1 = tmp
        head2 = p1
        
        #merge two lists
        pf = head1
        pe = head2
        while pe:
            temp1 = pf.next
            temp2 = pe.next
            pf.next = pe
            pe.next = temp1
            pf = temp1
            pe = temp2
        
        
            
