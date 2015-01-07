class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if len(num) == 0:
            return []
        elif len(num) == 1:
            return [num]
        res = []
        num.sort()
        pre = 99999
        for i in range(len(num)):
            if pre == num[i]:
                continue
            pre = num[i]
            for j in self.permuteUnique(num[0:i]+num[i+1::]):
                    res.append([num[i]]+j)
        return res
