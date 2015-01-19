class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        s=s.strip()
        
        i = 0
        e = len(s)-1
        
        if i>e:
            return False
        
        elif s[0] == '+' or s[0] == '-':
            i+=1
        
        num=False
        dot=False
        exp=False
        
        while i<=e:
            temp = s[i]
            if temp.isdigit():
                num = True
            elif temp == '.':
                if dot or exp:
                    return False
                dot = True
            elif temp == 'e':
                if exp or num == False:
                    return False
                exp = True
                num = False
            elif temp == '+' or temp == '-':
                if s[i-1]!='e':
                    return False
            else:
                return False
            i+=1
        return num
