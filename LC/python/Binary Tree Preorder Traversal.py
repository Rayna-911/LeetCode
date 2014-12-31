# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        res = []
        self.iterative(root,res)
        return res
    
    def iterative(self,root,res):
        stack = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root=stack.pop()
                root= root.right
        return res


        
