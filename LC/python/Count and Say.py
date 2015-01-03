class Solution:
    # @return a string
    def count(self, s):
        count = 0
        t =''
        m = '?'
        for i in s:
            if i != m :
                if m != '?':
                    t = t+str(count)+m
                m=i
                count = 1
            else:
                count = count + 1
                
        return t+str(count)+m
        
    def countAndSay(self, n):
        s = '1'
        for i in range(2,n+1):
            s = self.count(s)
        return s
