class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    #dp
    def wordBreak(self, s, dict):
        res = [False for i in range(len(s)+1)] 
        res[0] = True
        for i in range(len(s)):
            for j in range(i,-1,-1):
                if res[j] and s[j:i+1] in dict:
                    res[i+1] = True
                    break
        return res[len(s)]
