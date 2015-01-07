class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
            
        minlenstr = 99999
        minstr = ''
        res = ''
        # find the min length of all strs
        for i in strs:
            if len(i)<minlenstr:
                minlenstr = len(i)
                minstr = i
        
        t = 0 
        flag = True
        for m in range (len(minstr)):
            for n in strs:
                if  minstr[m] == n[m]:
                    t += 1
                    if t == len(strs):
                        res = res+minstr[m]
                        t = 0 
                else:
                    t = 0 
                    flag = False
                    break
            if flag == False:
                break

        return res
        
        
