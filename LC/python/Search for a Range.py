class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        res = []
        if len(A) == 1 and target == A[0]:
            return [0,0]
        for i in range(len(A)):
            if A[i] == target:
                res.append(i)
        if res == []:
            return [-1,-1]
        else:
            return [min(res),max(res)]
                
        
