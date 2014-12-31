class Solution:
    # @return an integer
    def maxArea(self, height):
        v = 0
        left = 0
        right = len(height)-1
        while left<right:
            vol = abs(left-right) * min(height[left],height[right])
            if vol > v:
                v = vol
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return v
        
