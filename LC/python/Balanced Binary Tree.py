# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def calculate_height(self,root):
        if root == None:
            return 0
        else:
            return max(self.calculate_height(root.right),self.calculate_height(root.left))+1
            
    def isBalanced(self, root):
        if root == None:
            return True
        elif abs(self.calculate_height(root.right) - self.calculate_height(root.left)) <= 1:
            return self.isBalanced(root.right) and self.isBalanced(root.left) 
        else:
            return False
        
            
        
