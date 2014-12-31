class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n == 0:
            return []
        
        res = []
        self.helper(n,n,'',res)
        return res
        
    def helper(self,left,right,item,res):
        if right < left:
            return 
        if left==0 and right==0:
            res.append(item)
        if left > 0:
            self.helper(left-1, right, item+'(', res)
        if right > 0:
            self.helper(left, right-1, item+')',res)
        
        
