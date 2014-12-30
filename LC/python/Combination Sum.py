class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    
    # dfs
    def combinationSum(self, candidates, target):
        
        def findRec(ans,target,t):
            flag = 0
            n = 0
            while t > 0:
                flag = 0
                for m in candidates:
                    if m == target:
                        ans.append(m)
                        flag += 1
                if flag == 0:
                    if n < len(candidates):
                        target -= candidates[n]
                        n +=1
                    else:
                        ans = []
                if target == 0:
                    break
                t-=1
            return ans
            
        if len(candidates) == 0:
            return [[]]
        
        res = []
        i = 1
        while i <= target:
            tmp = findRec([],target,i)
            tmp.sort()
            if tmp not in res:
                res.append(tmp)
            i+=1
        return res

a = Solution()
b = a.combinationSum([2,3],6)
print(b)

