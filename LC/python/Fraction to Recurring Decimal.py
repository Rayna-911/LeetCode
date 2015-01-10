class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if numerator%denominator == 0:
            return str(numerator / denominator)[:-2]
        
        ans = str(numerator / denominator)
        ans=ans.split('.')
        #print(len(ans[1]))
        s = ''
        if len(ans[1]) == 1:
            if ans[1] == '0':
                s= ''
            else:
                s = s+ans[1]
        else:
            first = ans[1][0]
            if ans[1].count(first) == len(ans[1]):
                s = s+'('+first+')'
            else:
                s = ans[1]
        return ans[0]+'.'+s

a = Solution()
b = a.fractionToDecimal(1,5)
print(b)
