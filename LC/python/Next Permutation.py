class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if len(num) < 2:
            return num
        
        for i in range(len(num)-2,-1,-1):
            if num[i]<num[i+1]:                         # if there exists a decreasing pair from tail, e.g. 145332 
                for j in range(len(num)-1,i,-1):        # find the first one which is larger than 4 from tail, which is 5 in the example
                    if num[j]>num[i]:
                        num[i],num[j] = num[j],num[i]   # reorder 45 to 54
                        left = i+1                      # reverse all items behind 4, which will be 154233
                        right = len(num)-1
                        while left < right:
                            num[left],num[right] = num[right],num[left]
                            left += 1
                            right -= 1
                        return num
        num.sort()
        return num
        
