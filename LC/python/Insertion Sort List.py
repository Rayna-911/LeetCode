# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head == None or head.next == None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        p = head
        
        while p.next:
            if p.next.val<p.val:
                pre = dummy
                while pre.next.val <p.next.val:
                    pre = pre.next
                
                tmp = p.next
                p.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                p=p.next
        return dummy.next
