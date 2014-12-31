class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if len(num) < 2:
            return 0
        elif len(num) == 2:
            if num[0] == max(num):
                return 0
            else: 
                return 1
        else:
            for i in range(1,len(num)-1):
                if num[i]>num[i-1] and num[i]>num[i+1]:
                    return i
                else:
                    return num.index(max(num))
        
