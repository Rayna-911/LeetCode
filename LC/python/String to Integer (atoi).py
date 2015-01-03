class Solution:
    # @return an integer
    def atoi(self, str):
        str1 = []
        str=str.strip()
        for i in range(0,len(str)):
            if str[i] in ['0','1','2','3','4','5','6','7','8','9','.','-','+']:
                str1.append(str[i])
            else:
                break
        Vrange = 2**31
        if len(str1) == 1 and str1[0].isdigit():
            return int(str1[0])
        elif len(str1) > 1  and str1[1].isdigit():
            if -Vrange <= int(''.join(str1)) < Vrange:
                return int(''.join(str1))
            elif int(''.join(str1)) >= Vrange:
                return Vrange-1
            elif int(''.join(str1)) < -Vrange:
                return -Vrange
            else:
                return 0
        else:
            return 0
        
                
       
