class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) == 0:
            return []
        elif len(num) == 1:
            return [num]
        
        res = []
        for i in range(len(num)):
            for j in self.permute(num[0:i]+num[i+1::]):
                res.append([num[i]] + j)
        return res
        
        
