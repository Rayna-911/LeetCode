# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        def dfs(root,tmp,string):
            if root == None:
                return
            string.append(root.val)
            tmp += root.val
            if root.left == None and root.right == None:
                if tmp == sum:
                    res.append(list(string))
            else:
                dfs(root.left,tmp,string)
                dfs(root.right,tmp,string)
            string.pop()
        
        if root == None:
            return []
        res = []
        dfs(root,0,[])
        return res
