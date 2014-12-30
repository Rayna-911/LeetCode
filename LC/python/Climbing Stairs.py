class Solution:
    # @param n, an integer
    # @return an integer
    #dp: f(n) = f(n-1)+f(n-2)
    def climbStairs(self, n):
        res = [1 for i in range(n+1)]
        for i in range(2,n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]
        
        
