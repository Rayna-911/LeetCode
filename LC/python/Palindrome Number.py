class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x<0:
            return False
        m = x
        n = 0
        while m!=0:
            m=m/10
            n = n+1
        
        if n <=1:
            return True
        else:
            t = 0
            i = 0
            while i< n/2: 
                t = t*10 + x%10
                x /=10
                i+=1
        if n%2 != 0:
            x/=10
        
        if x == t:
            return True
        else: 
            return False
        
            
        
        
