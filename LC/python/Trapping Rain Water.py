class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        sum = 0
        left = [0 for i in range(len(A))]
        leftmax = 0
        rightmax = 0
        
        for i in range(len(A)):
            if A[i]>leftmax:
                leftmax = A[i]
            left[i] = leftmax
        
        for i in reversed(range(len(A))):
            if A[i]>rightmax:
                rightmax = A[i]
            if min(rightmax, left[i]) > A[i]:
                sum += min(rightmax, left[i])-A[i]
            
        return sum
        
