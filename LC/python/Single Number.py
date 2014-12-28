class Solution:
    # @param A, a list of integer
    # @return an integer
    
    # bitwise operation
    def singleNumber(self, A):
        # XOR is needed
        ans = A[0]
        for i in range(1,len(A)):
            ans = ans ^ A[i]
        return ans
