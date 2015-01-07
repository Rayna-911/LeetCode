class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if len(s) == 0:
            return ''
            
        s = s.split()
        i = 1
        while i < len(s):
            s.insert(i,' ')
            i+=2
            
        res = ''
        for i in s:
            res = i+res
        return res
