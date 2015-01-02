class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        def dfs(num,string,res):
            if num == len(digits):
                res.append(string)
                return
            for i in dict[digits[num]]:
                dfs(num+1,string+i,res)
                
        dict = {'1':[], 
                '2':['a','b','c'], 
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z'],
                '0':[]}
        
        if len(digits) == 0:
            return ['']
        
        res = []
        dfs(0,'',res)
        return res
            
        
                
                
