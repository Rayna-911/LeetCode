# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.dfs(1,n)
    def dfs(self,start,end):
        if start > end:
            return [None]
        res = []
        for val in range(start,end+1):
            left = self.dfs(start,val-1)
            right = self.dfs(val+1,end)
            for i in left:
                for j in right:
                    root = TreeNode(val)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
        
