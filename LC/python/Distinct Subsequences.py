class Solution:
    # @return an integer
    #dp res[i][j] = n means it has n situations where T[:i+1] is the substring of S[:i+1]
    def numDistinct(self, S, T):
        res = [[0 for j in range(len(T)+1)] for i in range(len(S)+1)]
        for i in range(len(S)+1): #empty is the substring of any string
            res[i][0] = 1
            
        for i in range(1,len(S)+1):
            for j in range(1, min(i+1,len(T)+1)):
                if S[i-1] == T[j-1]:
                    res[i][j] = res[i-1][j]+res[i-1][j-1]
                else:
                    res[i][j] = res[i-1][j]
                
        return res[len(S)][len(T)]
        
