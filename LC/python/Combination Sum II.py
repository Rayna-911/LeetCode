class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        self.dfs(candidates,target,[],0,0,res)
        return res
    
    def dfs(self,candidates,target,sub,sum,index,res):
        if sum == target:
            res.append(list(sub))
            return
        for i in range(index,len(candidates)):
            if (i == index or candidates[i] != candidates[i-1]) and sum + candidates[i] <= target:
                sub.append(candidates[i])
                self.dfs(candidates,target,sub,sum+candidates[i],i+1,res)
                sub.pop()

