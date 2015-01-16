class Solution:
    # @return an integer
    #dp
    def minDistance(self, word1, word2):
        res = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        for i in range(len(word1)+1):
            res[i][0] = i #delete n times
        for i in range(len(word2)+1):
            res[0][i] = i #insert n times
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word2[j-1] == word1[i-1]:
                    res[i][j] = min(res[i-1][j]+1,res[i][j-1]+1,res[i-1][j-1])
                else:
                    res[i][j] = min(res[i-1][j]+1,res[i][j-1]+1,res[i-1][j-1]+1)
        return res[len(word1)][len(word2)]
