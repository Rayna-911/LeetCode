class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        self.res = []
        self.dfs(s,[])
        return self.res
        
    def isPalindrome(self,s):
        for i in range(len(s)):
            if s[i] != s[-i-1]:
                return False
        return True
        
    def dfs(self,s,string):
        if len(s) == 0:
            self.res.append(string)
        for i in range(1,len(s)+1):
            sub = s[:i]
            if self.isPalindrome(sub):
                self.dfs(s[i:],string+[sub])
