# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        def dfs(indin,indpost,elem):
            if elem == 0:
                return None
            right = 0
            root = TreeNode(postorder[indpost])
            for i in range(indin,(indin-elem),-1):
                if inorder[i] == root.val:
                    break
                right+=1
            root.left = dfs(indin-right-1,indpost-right-1,elem-right-1)
            root.right = dfs(indin,indpost-1,right)
            return root
        return dfs(-1,-1,len(postorder))
        
