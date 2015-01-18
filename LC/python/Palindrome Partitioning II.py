class Solution:
    # @param s, a string
    # @return an integer
    #dp
    def minCut(self, s):
        dp = [0 for i in range(len(s)+1)]
        p = [[False for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)+1):
            dp[i] = len(s)-i
        for i in reversed(range(len(s))):
            for j in range(i,len(s)):
                if (s[i] == s[j] and ((j-i)<=2 or p[i+1][j-1] == True)):
                    p[i][j] = True
                    dp[i] = min(dp[i],dp[j+1]+1)
        return dp[0]-1
        
    
        
