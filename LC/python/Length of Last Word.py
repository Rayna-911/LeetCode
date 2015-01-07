class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s=s.split()
        if s != []:
            return len(s[-1]) 
        else:
            return 0
        
