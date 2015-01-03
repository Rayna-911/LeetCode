class Solution:
    # @return a list of integers
    #dp
    def getRow(self, rowIndex):
        if rowIndex == 0 : return [1]
        elif rowIndex == 1 : return [1,1]
        else:
            lst = [[] for i in range(rowIndex+1)]
            lst[0] = [1]
            lst[1] = [1,1]
            for i in range(2,rowIndex+1):
                lst[i] = [1 for m in range(i+1)]
                for j in range(1,i):
                    lst[i][j] = lst[i-1][j-1]+lst[i-1][j]
        return lst[rowIndex]
        
