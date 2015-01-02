# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        def dfs(root,minV,maxV):
            if root == None:
                return True
            if root.val<=minV or root.val>=maxV:
                return False
            return dfs(root.left,minV,root.val) and dfs(root.right,root.val,maxV)
            
        return dfs(root,float("-inf"),float("inf"))
