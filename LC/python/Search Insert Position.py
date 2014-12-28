class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        less = -1
        great = -1
        for i in range(len(A)):
            if A[i] > target:
                great = i
            elif A[i] < target:
                less = i
            else:
                return i
        if great == -1 and less != -1:
            return len(A)
        if less == -1 and great != -1:
            return 0
        else:
            return less+1
