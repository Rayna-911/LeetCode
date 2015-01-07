class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        (digits[-1],full) = self.addone(digits[-1]+1,0)
        for i in range(len(digits)-2,-1,-1):
            (digits[i],full) = self.addone(digits[i],full)
        if full == 1:
            digits.insert(0,1)
        return digits
        
    def addone(self,digit,full):
        res = digit + full
        digit = res % 10
        full = res / 10
        return (digit, full)
        
