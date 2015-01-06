# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    #soln1:convert to array
    #soln2:find mid and recursion to build bst
    def sortedListToBST(self, head):
        m = self.getLen(head)
        return self.buildBST(head,m,ListNode(0))
        
    def buildBST(self,head,cnt,res):
        if cnt == 0:
            res.next = head
            return None
        left = self.buildBST(head,cnt//2,res)
        root = TreeNode(res.next.val)
        res.next=res.next.next 
        right = self.buildBST(res.next,cnt-cnt//2-1,res)
        root.left = left
        root.right = right
        return root
        
    def getLen(self,head):
        size = 0
        while head:
            size+=1
            head = head.next
        return size
