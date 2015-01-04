class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        res = [0 for i in range(len(num1)+len(num2))]
        ans = []
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j] += int(num1[i]) * int(num2[j])
    
        flag = 0
        for i in range(len(res)):
            ans.insert(0,str((res[i]+flag)%10))
            flag = (res[i]+flag)/10
            
        if flag > 0:
            ans.insert(0,str(flag))
            
        while ans[0] == '0' and len(ans) > 1:
            del ans[0]
        
        return ''.join(ans)
