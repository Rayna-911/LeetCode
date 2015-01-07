class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        left = 0
        right = len(A)
        while left < right:
            mid = (left + right)/2
            if A[mid] == target:
                return True
            elif A[left]<A[mid]:
                if A[left] <= target and target < A[mid]:
                    right = mid
                else:
                    left = mid+1
            elif A[left] > A[mid]:
                if A[mid] < target and target <= A[right-1]:
                    left = mid+1
                else:
                    right = mid
            else:
                left = left +1
        return False
