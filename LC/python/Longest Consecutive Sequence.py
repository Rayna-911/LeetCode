class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        dict = {x:False for x in num}
        m = -1
        for i in dict:
            if dict[i]==False:
                curr = i-1
                lenleft = 0
                while curr in dict:
                    lenleft += 1
                    dict[curr] = True
                    curr -= 1
                curr = i+1
                lenright = 0
                while curr in dict:
                    lenright += 1
                    dict[curr] = True
                    curr += 1
                m = max(m,lenleft+lenright+1)
        return m
