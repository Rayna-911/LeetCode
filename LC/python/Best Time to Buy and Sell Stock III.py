class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
            
        f = []
        minV = prices[0]
        maxP = -1
        for i in prices:
            minV = min(i,minV)
            maxP = max(i-minV,maxP)
            f.append(maxP)
        
        b = []
        maxV = prices[len(prices)-1]
        maxP = -1
        for i in reversed(prices):
            maxV = max(i,maxV)
            maxP = max(maxV-i,maxP)
            b.insert(0,maxP)
        
        res = f[-1] 
        for i in range (len(f)-1):
            res = max(res,f[i]+b[i+1])
        return res
            
        
