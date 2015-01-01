# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    
    #dfs
    #def preorder(self, root, level, result):
    #    if root != None:
    #        if len(result) < level+1: 
    #            result.append([])
    #        result[level].append(root.val)
    #        self.preorder(root.left,level+1, result)
    #        self.preorder(root.right, level+1, result)
    
    #def levelOrder(self, root):
    #    result = []
    #    self.preorder(root, 0 , result)
    #    return result
    
    #bfs
    def levelOrder(self, root):
        if root == None:
            return []
        
        res = [[root.val]]
        sub = []
        q1 = [root]
        
        while q1 != []:
            q2 = []
            while q1 != []:
                tmp = q1.pop(0)
                if tmp.left:
                    q2.append(tmp.left)
                if tmp.right:
                    q2.append(tmp.right)
            if q2 != []:
                res.append([])
            for i in q2:
                res[-1].append(i.val)
            q1 = q2
        return res
