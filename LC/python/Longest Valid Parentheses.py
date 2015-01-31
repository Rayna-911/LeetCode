class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        tmp = -1
        maxlen = 0
        for i in range(0,len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack == []:
                    tmp = i
                else:
                    stack.pop()
                    if stack ==[]:
                        maxlen = max(maxlen, i-tmp)
                    else:
                        maxlen = max(maxlen, i-stack[len(stack)-1])
        return maxlen
                    
