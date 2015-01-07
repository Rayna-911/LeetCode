class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        def dfs(sub,start,depth):
            if sub not in res:
                res.append(sub)
            if depth == len(S):
                return
            for i in range(start,len(S)):
                dfs(sub+[S[i]],i+1,depth+1)
        S.sort()
        res=[]
        dfs([],0,0)
        return res
        
