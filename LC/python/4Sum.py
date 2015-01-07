class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if len(num)<4:
            return []
        m = len(num)
        res = set()
        dict = {}
        num.sort()
        for i in range(m):
            for j in range(i+1,m):
                key = num[i]+num[j]
                if key not in dict:
                    dict[key] = [(i,j)]
                else:
                    dict[key].append((i,j))
        for i in range(m):
            for j in range(i+1,m):
                T = target - num[i] - num[j]
                if T in dict:
                    for n in dict[T]:
                        if n[0]>j:
                            res.add((num[i],num[j],num[n[0]],num[n[1]]))
        return [list(i) for i in res]
                    
                    
        
