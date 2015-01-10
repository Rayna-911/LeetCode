class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    
    # dfs
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        self.dfs(candidates,target,[],0,0,res)
        return res
        
    def dfs(self,candidates,target,sub,sum,index,res):
        if sum == target:
            res.append(list(sub))
        for i in range(index,len(candidates)):
            if sum + candidates[i]> target:
                break
            sub.append(candidates[i])
            self.dfs(candidates,target,sub,sum+candidates[i],i,res)
            sub.pop()
