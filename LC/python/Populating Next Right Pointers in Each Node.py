# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

    #dfs
#class Solution:
    # @param root, a tree node
    # @return nothing
#    def connect(self, root):
#        if root == None:
#            return 
#        res = []
#        self.dfs(0,root,res)
#        for i in range(len(res)):
#            for j in range(len(res[i])):
#                if j != len(res[i])-1:
#                    res[i][j].next = res[i][j+1]
#                else:
#                    res[i][j].next = None
                    
#    def dfs(self,level,root,res):
#        if root:
#            if len(res)<level+1:
#                res.append([])
#            res[level].append(root)
#            self.dfs(level+1,root.left,res)
#            self.dfs(level+1,root.right,res)

    #bfs
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        q1 = [root]
        
        while q1:
            q2 = []
            while q1:
                tmp = q1.pop(0)
                if tmp.left:
                    q2.append(tmp.left)
                if tmp.right:
                    q2.append(tmp.right)
            q1 = q2
            for i in range(len(q2)):
                if i != len(q2)-1:
                    q2[i].next = q2[i+1]
                else:
                    q2[i].next = None
            
            
