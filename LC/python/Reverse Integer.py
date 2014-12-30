class Solution:
    # @return an integer
    def reverse(self, x):
        if x >= 0:
            flag = True
        else:
            flag = False
            x = -x
        temp = 0
        while x != 0:
            temp = temp *10 + x%10
            x=x/10
        if temp>(2**(32)/2):
            return 0
        elif flag:
            return temp
        else:
            return -temp
            
        
