# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        
        if headA == None or headB == None:
            return None
                
        m = self.getListlen(headA)
        n = self.getListlen(headB)
        
        pa = headA
        pb = headB
        
        if m>n:
            for i in range(m-n):
                pa = pa.next
        else:
            for i in range(n-m):
                pb = pb.next
        
        while pa and pb:
            if pa!=pb:
                if pa.next != None and pb.next != None:
                    pa = pa.next
                    pb = pb.next
                else:
                    break
            else:
                return pa
            
        return None
        
    def getListlen(self,head):
        size = 0
        p = head
        while p.next:
            size+=1
            p=p.next
        return size
