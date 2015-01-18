# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        Solution.sum = -9999
        if root == None:
            return 0
        self.maxS(root)
        return Solution.sum
        
    def maxS(self,root):
        if root == None:
            return 0
        sum = root.val
        lmax = 0
        rmax = 0
        if root.left:
            lmax = self.maxS(root.left)
            if lmax > 0:
                sum += lmax
        if root.right:
            rmax = self.maxS(root.right)
            if rmax >0:
                sum += rmax
        if sum > Solution.sum:
            Solution.sum = sum
        return max(root.val,max(root.val+lmax,root.val+rmax))
        
    
        
        
        
