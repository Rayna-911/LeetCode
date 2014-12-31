class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        return self.comb([],n,k,1)
            
    def comb(self,ans,n,k,i):
        if k == 0:
            return [ans]
        if i>n:
            return []
        return self.comb(ans,n,k,i+1)+self.comb(ans+[i],n,k-1,i+1)
