class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        num = 0 
        n = 0
        i = 0 
        if len(haystack) < len(needle):
            return -1
        elif needle == '':
            return 0
            
        while (i < len(haystack) and num < len(needle)):
            if haystack[i] == needle[num]:
                n += 1
                if n == len(needle):
                    return i-len(needle)+1
                i +=1
                num +=1
            else:
                i = i -n+1
                num = 0
                n=0
        return -1
                
            
        
