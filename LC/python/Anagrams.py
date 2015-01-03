class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        dict = {}
        res = []
        for i in strs:
            word = ''.join(sorted(i))
            if word not in dict:
                dict[word] = [i]
            else:
                dict[word] += [i]
                
        for i in dict:
            if len(dict[i]) >= 2:
                res += dict[i]
            
        return res
