class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        self.res = []
        self.dfs(s,dict,'')
        return self.res
                
    def dfs(self,s,dict,strslist):
        if self.canBreak(s,dict):
            if s == '':
                self.res.append(strslist[1:])
            for i in range(1,len(s)+1):
                if s[:i] in dict:
                    self.dfs(s[i:],dict,strslist+' '+s[:i])
        
    def canBreak(self,s,dict):
        res = [False for i in range(len(s)+1)] 
        res[0] = True
        for i in range(len(s)):
            for j in range(i,-1,-1):
                if res[j] and s[j:i+1] in dict:
                    res[i+1] = True
                    break
        return res[len(s)]
