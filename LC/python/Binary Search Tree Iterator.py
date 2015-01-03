# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.leftNode(root)
            
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack
        
    # @return an integer, the next smallest number
    def next(self):
        curr = self.stack.pop()
        self.leftNode(curr.right)
        return curr.val

    def leftNode(self,node):
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
