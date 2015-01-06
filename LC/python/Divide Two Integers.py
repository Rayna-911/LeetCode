class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            if abs(dividend) < abs(divisor):
                return 0
        sum = 0
        cnt = 0
        res = 0
        a = abs(dividend)
        b = abs(divisor)
        while a>=b:
            sum = b
            cnt = 1
            while sum+sum <= a:
                sum += sum
                cnt+=cnt
            a -= sum
            res += cnt
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            res = 0-res
        if res >= 2**31:
            res = 2**31-1
        if res <= -2**31+1:
            res = -2**31
        return res
