class Solution:
    # @return a string
    def convertToTitle(self, num):
        res = ''
        while num != 0 :
            res = chr(ord('A') + (num-1) % 26) + res 
            num = (num-1) / 26
        return res
        
        
