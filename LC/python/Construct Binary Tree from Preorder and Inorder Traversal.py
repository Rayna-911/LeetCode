# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        def dfs(indpre,indin,element):
            if element == 0:
                return None
            left = 0
            res = TreeNode(preorder[indpre])
            for i in range(indin,indin+element):
                if preorder[indpre] == inorder[i]:
                    break
                left+=1
            res.left = dfs(indpre+1,indin,left)
            res.right = dfs(indpre+left+1,indin+left+1,element-left-1)
            return res
        return dfs(0,0,len(preorder))
        
