class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        curr = 0
        maxValue = -9999
        
        for i in A:
            if curr < 0:
                curr =0
            curr = curr +i
            maxValue = max(curr,maxValue)
        return maxValue
