class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        res = []
        if numRows == 0:
            return res
        current = [1]
        
        res.append(current)
        
        for i in range(1,numRows):
            pre = current
            current = [1]
            for j in range(0,i-1):
                current.append(pre[j]+pre[j+1])
            current.append(1)
            res.append(current)
        
        return res
        
        
