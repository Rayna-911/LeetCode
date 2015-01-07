class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head == None or head.next == None:
            return head
        
        dummy = ListNode(0)
        tmp = dummy
        
        dummy1 = ListNode(0)
        less = dummy1
        
        p = head
        
        while p:
            if p.val < x:
                tmp.next = p
                tmp = tmp.next
                p = p.next
                tmp.next = None
            else:
                less.next = p
                less = less.next
                p = p.next
                less.next = None            
        
        tmp.next = dummy1.next
        return dummy.next
