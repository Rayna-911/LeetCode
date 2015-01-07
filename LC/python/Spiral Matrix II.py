class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0:
            return []
        
        res = [[0 for i in range(n)] for i in range(n)]
        
        up = 0
        left = 0
        bottom = n
        right = n
        direct = 0
        
        j = 1
        while j < n**2+1:
            if direct == 0:
                for i in range(left,right):
                    res[up][i] = j
                    j += 1
                up +=1
            if direct == 1:
                for i in range(up,bottom):
                    res[i][right-1] = j
                    j+=1
                right -=1
            if direct == 2:
                for i in range(right-1,left-1,-1):
                    res[bottom-1][i] = j
                    j+=1
                bottom -= 1
            if direct == 3:
                for i in range(bottom-1,up-1,-1):
                    res[i][left] = j
                    j+=1
                left+=1
            direct = (direct+1)%4
        return res
                
        
        
