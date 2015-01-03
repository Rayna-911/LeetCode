class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s) == 0:
            return True
        else:
            s = s.lower()
            reverse = ''
            norm = ''
            flag = True
            for i in s:
                if i.isalpha() or i.isdigit():
                    reverse = reverse+i
                    norm = i+norm
                else:
                    continue
            if reverse == norm:
                return True
            else: return False
