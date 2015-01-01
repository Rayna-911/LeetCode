class Solution:
    # @return an integer
    #dp
    #catalan num
    def numTrees(self, n):
        if n < 2:
            return 1
        elif n == 2:
            return 2
        else:
            res = [0 for i in range(n+1)]
            res[0] = 1
            res[1] = 1
            res[2] = 2
            for i in range(3,n+1):
                for j in range(i):
                    res[i] = res[i]+res[j]*res[i-j-1]
                
        return res[n]
        
