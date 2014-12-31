# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        res = []
        self.iterative(root,res)
        return res
        
    def iterative(self,root,res):
        stack = []
        pre = None
        if root:
            stack.append(root)
            while stack:
                curr = stack[-1]
                if (curr.left == None and curr.right == None) or (pre and (pre == curr.left or pre == curr.right)):
                    res.append(curr.val)
                    pre = curr
                    stack.pop()
                else:
                    if curr.right:
                        stack.append(curr.right)
                    if curr.left:
                        stack.append(curr.left)
                
        return res
                
        
