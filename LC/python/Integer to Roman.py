class Solution:
    # @return a string
    def intToRoman(self, num):
        nums = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        symbol = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        res = ''
        for i in range(len(nums)-1,-1,-1):
            while num >= nums[i]:
                num -= nums[i]
                res += symbol[i]
        return res
            
