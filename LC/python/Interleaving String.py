class Solution:
    # @return a boolean
    #dp:res[i][j] means if s1[0...i-1] and s2[0...j-1] can become valid s3[0...i+j-1]
    def isInterleave(self, s1, s2, s3):
        if len(s1)+ len(s2) != len(s3):
            return False
        res = [[False for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        res[0][0] = True
        for i in range(1,len(s1)+1):
            res[i][0] = (res[i-1][0] and s3[i-1] == s1[i-1])
        for j in range(1,len(s2)+1):
            res[0][j] = (res[0][j-1] and s3[j-1] == s2[j-1])
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                res[i][j] = (res[i-1][j] and s3[i+j-1] == s1[i-1] ) or (res[i][j-1] and s3[i+j-1] == s2[j-1])
        return res[len(s1)][len(s2)]
