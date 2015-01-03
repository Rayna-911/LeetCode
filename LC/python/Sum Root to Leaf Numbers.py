# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        def dfs(root,Sum):
            if root == None:
                return
            Sum = Sum*10+root.val
            if root.left == None and root.right == None:
                self.res += Sum
            else:
                dfs(root.left,Sum)
                dfs(root.right,Sum)
        self.res = 0
        dfs(root,0)
        return self.res
        
