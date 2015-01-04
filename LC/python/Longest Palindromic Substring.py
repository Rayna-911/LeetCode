class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
            
        sub = ''
        for i in range(len(s)):
            len1 = len(self.getPalindromic(s,i,i))
            if len1 > len(sub):
                sub = self.getPalindromic(s,i,i)
            len2 = len(self.getPalindromic(s,i,i+1))
            if len2 > len(sub):
                sub = self.getPalindromic(s,i,i+1)
        return sub
                
    def getPalindromic(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]
