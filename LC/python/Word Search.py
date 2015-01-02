class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        def dfs(i,j,index):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[index] != board[i][j]:
                return False
            if index == len(word) -1:
                return True
            board[i][j] = '#'
            res = dfs(i+1,j,index+1) or dfs(i-1,j,index+1) or dfs(i,j+1,index+1) or dfs(i,j-1,index+1)
            board[i][j] = word[index]
            return res
            
        res = False
        for m in range(len(board)):
            for n in range(len(board[0])):
                res = res or dfs(m,n,0)
        return res
        
        
        
