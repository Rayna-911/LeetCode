class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x < 2:
            return x
        
        left = 0 
        right = x/2
        
        if right**2 == x:
            return right
        
        while left <= right:
            mid = (left+right)/2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                left = mid+1
            else:
                right = mid-1
                
        return right
                
