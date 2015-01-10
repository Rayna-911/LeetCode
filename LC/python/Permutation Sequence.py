class Solution:
    # @return a string
    def getPermutation(self, n, k):
        num = [str(x) for x in range(1,n+1)]
        factorial = [1]
        for i in range(1,n+1):
            factorial.append(factorial[i-1]*i)
        self.rec(n,k-1,num,factorial,0)
        return "".join(num)
        
            
    def rec(self,n,k,num,factorial,t):
        if k == 0 or t > n-1:
            return 
        else:
            s = k/factorial[n-t-1]
            p = num.pop(s+t)
            num.insert(t,p)
            k = k%factorial[n-t-1]
            self.rec(n,k,num,factorial,t+1)
            return
    
