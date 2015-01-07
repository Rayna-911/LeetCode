class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        def check(i,j,temp):
            for m in range(9):
                if board[i][m] == temp:
                    return False
                if board[m][j] == temp:
                    return False
            for n in range(3):
                for t in range(3):
                    if board[i/3*3+n][j/3*3+t] == temp:
                        return False
            return True
            
        for i in range(9):
            for j in range(9):
                temp = board[i][j]
                board[i][j] = 'D'
                if temp == '.':
                    continue
                res = check(i,j,temp)
                if res == False:
                    return False
                else:
                    board[i][j] = temp
        return True
                
    
        
            
            
        
