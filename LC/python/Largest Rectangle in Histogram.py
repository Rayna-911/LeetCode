class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        stack = []
        height.append(0)
        maxA = 0
        i = 0
        while i < len(height):
            #print(stack)
            if stack == [] or height[i]>=height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                tmp = stack.pop()
                if stack == []:
                    area = height[tmp] * i
                else:
                    print(i,stack[-1])
                    area = height[tmp] * (i-stack[-1]-1)
                maxA = max(maxA,area)
        return maxA
a = Solution()
b = a.largestRectangleArea([2,1,5,6,2,3])
