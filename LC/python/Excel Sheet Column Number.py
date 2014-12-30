class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        res = 0
        for i in range(len(s)):
            res = res*26+(ord(s[i])-64)
        return res
        
        
