class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if A == []:
            return 0
        
        minV = A[0]
        maxV = A[0]
        res = A[0]
        
        for i in range(1,len(A)):
            a = A[i] * minV
            b = A[i] * maxV
            c = A[i]
            
            minV = min(a,b,c)
            maxV = max(a,b,c)
            if res < maxV:
                res = maxV
        return res
