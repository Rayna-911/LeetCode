class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        up = 0
        left = 0
        bottom = len(matrix)
        right = len(matrix[0])
        direct = 0 
        res = []
        
        while True:
            if direct == 0:
                for i in range(left,right):
                    res.append(matrix[up][i])
                up+=1
            if direct == 1:
                for i in range(up,bottom):
                    res.append(matrix[i][right-1])
                right-= 1
            if direct == 2:
                for i in range(right-1, left-1,-1):
                    res.append(matrix[bottom-1][i])
                bottom-=1
            if direct == 3:
                for i in range(bottom-1,up-1,-1):
                    res.append(matrix[i][left])
                left+=1
            if up>=bottom or left>=right:
                return res
            else:
                direct = (direct+1) % 4
