class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if (m+n)%2 == 0:
            return (self.rec(A,B,(m+n)/2)+self.rec(A,B,(m+n)/2+1))*0.5
        else:
            return (self.rec(A,B,(m+n)/2+1))
        
    def rec(self,A,B,k):
        if len(A) > len(B):
            return self.rec(B,A,k)
        if len(A) <= 0:
            return B[k-1]
        if k <= 1 :
            return (min(A[0],B[0]))
        
        pa = min(k/2,len(A))
        pb = k - pa
        if A[pa-1] <= B[pb-1]:
            return self.rec(A[pa:],B,pb)
        else:
            return self.rec(A,B[pb:],pa)
            
