class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        n = []
        for i in num:
            if i not in n:
                n.append(i)
        print(n)
        dict ={}
        while n != []:
            i = n.pop()
            if (i - 1) in dict:
                dict[i-1] += 1
            elif (i + 1) in dict:
                dict[i+1] += 1
            else:
                dict[i] = 1
        return max(dict.values())

a = Solution()
print(a.longestConsecutive([1,0,-1]))
