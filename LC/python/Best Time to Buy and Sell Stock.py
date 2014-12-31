class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0 :
            return 0
            
        minValue = float("inf")
        maxProfit = 0

        for i in range(len(prices)):
            if prices[i] < minValue:
                minValue = prices[i]
            if maxProfit < prices[i] - minValue:
                maxProfit = prices[i] - minValue
        return maxProfit
        
