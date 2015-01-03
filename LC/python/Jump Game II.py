class Solution:
    # @param A, a list of integers
    # @return an integer
    
    #def jump(self, A):
    #    res = [999999 for i in range(len(A))]
    #    step = A[0]
    #    res[0] = A[0]
    #    for i in range(1,len(A)):
    #        for j in range(i):
    #            if A[j] >= i-j:
    #                res[i] = min(res[i],res[j]+1)
    #    return res[len(res)-1]
    
    
    def jump(self,A):
        curr = 0
        last = 0
        res = 0
        for i in range(len(A)):
            if i>last:
                last = curr
                res+=1
            curr = max(curr,i+A[i])
        return res
        
