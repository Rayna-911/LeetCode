class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        last = ""
        
        for i in range(0,len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if stack == []:
                    return False
                elif (s[i] == ")" and stack.pop() != "(") or (s[i] == "]" and stack.pop() != "[") or (s[i] == "}" and stack.pop() != "{"):
                    return False
                
        return not stack
                
        
        
        
        
