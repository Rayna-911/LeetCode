# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    #bfs
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        q1 = [root]
        res = [[root.val]]
        n=1
        
        while q1:
            q2 = []
            while q1:
                tmp = q1.pop(0)
                if tmp.left:
                    q2.append(tmp.left)
                if tmp.right:
                    q2.append(tmp.right)
            q1 = q2
            n +=1
            if q2 != []:
                res.append([])
            if n % 2 == 0:
                for i in range(len(q2)-1,-1,-1):
                    res[-1].append(q2[i].val)
            else:
                for i in range(len(q2)):
                    res[-1].append(q2[i].val)
            
        return res
        
