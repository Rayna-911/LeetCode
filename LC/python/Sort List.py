# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    #merge sort O(nlogn) Time
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        slow = head
        quick = head
        
        while quick.next and quick.next.next:
            slow = slow.next
            quick = quick.next.next
        head1 = head
        head2 = slow.next
        slow.next = None
        
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        head = self.merge(head1,head2)
        return head
    
    def merge(self,head1,head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        
        dummy = ListNode(0)
        p = dummy
        
        while head1 and head2:
            if head1.val<head2.val:
                p.next = head1
                head1 = head1.next
                p = p.next
            else:
                p.next = head2
                head2 = head2.next
                p = p.next
            
        if head1 == None:
            p.next = head2
        if head2 == None:
            p.next = head1
        return dummy.next
        
        
