class Solution:
    # @return a list of lists of string
    #board[1,3,0,2] means   [". Q . .",
    #                        ". . . Q",
    #                        "Q . . .",
    #                        ". . Q ."]
    def solveNQueens(self, n):
        def dfs(row, sub):
            if row == n:
                res.append(sub)
            for i in range(n):
                if set(row,i):
                    board[row] = i
                    s = '.'*n
                    dfs(row+1,sub + [s[:i] +'Q'+s[i+1:]] )
                
        def set(index,num):
            for i in range(index):
                if board[i]==num or abs(board[i]-num) == index - i:
                    return False
            return True
            
        board = [-1 for i in range(n)]
        res = []
        dfs(0,[])
        return res
        
