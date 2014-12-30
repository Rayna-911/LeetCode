class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        i = 0
        m = len(A)
        while i < m:
            if A[i] == 0:
                del A[i]
                A.insert(0,0)
            elif A[i] == 2:
                del A[i]
                A.insert(len(A),2)
                m -=1
                i-=1
            i +=1
            
            
            
        
