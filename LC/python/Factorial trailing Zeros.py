class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        if n <= 1 :
            return 0
        x = 5
        c5=0
        while n >= x:
            c5 = c5 + n/x
            x = 5*x
        return c5
