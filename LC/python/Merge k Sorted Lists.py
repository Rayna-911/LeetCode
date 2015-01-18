# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = []
        for i in lists:
            if i:
                heap.append((i.val,i))
        heapq.heapify(heap)
        
        head = ListNode(0)
        p = head
        
        while heap:
            curr = heapq.heappop(heap)
            p.next = ListNode(curr[0])
            p = p.next
            if curr[1].next:
                heapq.heappush(heap, (curr[1].next.val, curr[1].next))
        return head.next
            
        
