class Solution:
    # @return a string
    #when repeating in answer, mod repeats
    def fractionToDecimal(self, numerator, denominator):
        
        flag = 1
        if numerator*denominator<0:
            flag = -1
            
        num = abs(numerator)
        den = abs(denominator)
        
        dict = {}
        decimal = []
        loop = None
        
        i=0
        while True:
            decimal.append(str(num/den))
            i += 1
            num = 10*(num%den)
            
            if num == 0:
                break
            
            if num in dict:
                start = dict.get(num)
                loop = ''.join(decimal[start:i])
                break
            dict[num] = i
        
        res = decimal[0]
        if len(decimal)>1:
            res = res + '.'
        if loop:
            res = res + ''.join(decimal[1:len(decimal)-len(loop)]) + '(' + loop + ')'
        else:
            res = res + ''.join(decimal[1:])
        if flag < 0:
            res = '-'+ res
        return res
        
