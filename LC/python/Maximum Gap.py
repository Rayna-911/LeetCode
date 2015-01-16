class Solution:
    # @param num, a list of integer
    # @return an integer
    #sort
    #def maximumGap(self, num):
    #    if len(num)<2:
    #        return 0
    #    num.sort()
    #    m=0
    #    for i in range(0,len(num)-1):
    #        m = max(m,num[i+1]-num[i])
    #    return m
    def maximumGap(self, num):
        if len(num) < 2:
            return 0
        A = min(num)
        B = max(num)
        r = max(1,int((B-A-1)/(len(num)-1))+1)
        l = (B-A)/r+1
        backet = [None] * l
        
        for k in num:
            loc = (k-A)/r
            b = backet[loc]
            if b is None:
                b = {"max":k,"min":k}
                backet[loc] = b
            else:
                b["max"] = max(b["max"],k)
                b["min"] = min(b["min"],k)
        
        m = 0
        for i in range(l):
            if backet[i] is None:
                continue
            j = i+1
            while j<l and backet[j] is None:
                j=j+1
            if j < l:
                m = max(m, backet[j]["min"]-backet[i]["max"])
            i = j
        return m
        
