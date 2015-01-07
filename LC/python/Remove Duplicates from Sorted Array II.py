class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 2:
            return len(A)
        pre = 1
        curr = 2
        while curr< len(A):
            if A[curr] == A[pre] and A[curr] == A[pre-1]:
                curr +=1
            else:
                pre+=1
                A[pre] = A[curr] 
                curr+=1
        return pre+1
            
        
