class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for i in range(len(tokens)):
            if tokens[i]!='+' and tokens[i]!='-' and tokens[i]!='*' and tokens[i]!='/':
                stack.append(int(tokens[i]))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if tokens[i] == '+':
                    tmp = num2+num1
                elif tokens[i] == '-':
                    tmp = num2-num1
                elif tokens[i] == '*':
                    tmp = num2*num1
                elif tokens[i] == '/':
                    if num2*num1<0:
                        tmp = -((-num2)/num1) #in python:-1/2 = -1
                    else:
                        tmp = num2/num1
                stack.append(tmp)
        return stack.pop()
