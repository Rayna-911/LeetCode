class Solution:
    # @param s, a string
    # @return an integer
    #dp
    def numDecodings(self, s):
        if s == '' or s[0] == '0':
            return 0
            
        res = [0 for i in range(len(s)+1)]
        res[0] = 1
        res[1] = 1
        
        for i in range(2,len(s)+1):
            if (int(s[i-2:i])>9 and int(s[i-2:i])<27) and s[i-1] != '0':
                res[i] = res[i-1]+res[i-2]
            elif int(s[i-2:i])==10 or int(s[i-2:i])==20:
                res[i] = res[i-2]
            elif s[i-1] != '0':
                res[i] = res[i-1]
            else:
                return 0
        return res[len(s)]
