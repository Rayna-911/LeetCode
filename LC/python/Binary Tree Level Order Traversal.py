# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    
    #dfs or bfs
    #actually, preorder is kind of dfs
    def preorder(self, root, level, result):
        if root != None:
            if len(result) < level+1: 
                result.append([])
            result[level].append(root.val)
            self.preorder(root.left,level+1, result)
            self.preorder(root.right, level+1, result)
    
    def levelOrder(self, root):
        result = []
        self.preorder(root, 0 , result)
        return result
      
            
        
