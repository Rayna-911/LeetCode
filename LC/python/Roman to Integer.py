class Solution:
    # @return an integer
    def romanToInt(self, s):
        #when left is less than right, right - left
        #else: right + left
        num = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum = 0
        last = 0
        for i in range(len(s)-1,-1,-1):
            if last > num[s[i]]:
                sum = sum-num[s[i]]
            else:
                sum = sum+num[s[i]]
            last = num[s[i]]
        return sum
            
        
