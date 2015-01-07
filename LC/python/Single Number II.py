class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        dict = {}
        for i in A:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] +=1
        for i in dict:
            if dict[i] == 1:
                return i
        
