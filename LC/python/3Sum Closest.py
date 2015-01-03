class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        res = 0
        mindiff = 99999
        for i in range(len(num)):
            left = i+1 
            right = len(num)-1
            
            while left < right:
                sum = num[i]+num[left]+num[right]
                diff = abs(sum-target)
                if diff<mindiff:
                    mindiff = diff
                    res = sum
                if sum == target:
                    return sum
                elif sum < target:
                    left +=1
                else:
                    right-=1
        return res
                
