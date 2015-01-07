# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        elif root.left == None and root.right == None:
            return True
        elif root.left != None and root.right!= None:
            return self.symmetric(root.left,root.right)
        else: 
            return False
            
    def symmetric(self,left,right):
        if left == None and right == None:
            return True
        elif left != None and right != None:
            return (left.val == right.val and self.symmetric(left.left, right.right) and self.symmetric(left.right, right.left))
        return False
        
