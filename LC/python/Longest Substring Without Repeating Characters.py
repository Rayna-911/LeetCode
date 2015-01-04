class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) < 2:
            return len(s)
        
        maxV = 0
        dict ={}
        last = -1
        for i in range(len(s)):
            if s[i] in dict and last < dict[s[i]]:
                last = dict[s[i]]
            if i - last > maxV:
                maxV = i - last
            dict[s[i]] = i
        return maxV
