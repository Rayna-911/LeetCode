class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        def dfs(s, part, string, res):
            if part == 4:
                if s == '':
                    res.append(string[:-1])
                return
            for i in range(1,4):
                if i <= len(s):
                    if int(s[:i])<=255:
                        dfs(s[i:], part+1, string+s[:i]+'.',res)
                    if s[0] == '0':
                        break
        res = []
        dfs(s,0,'',res)
        return res
