class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        
        profit = 0
        for i in range(0,len(prices)-1):
            profit += max(0,(prices[i+1] - prices[i]))
        return profit
