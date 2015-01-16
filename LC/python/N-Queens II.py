class Solution:
    # @return an integer
    def totalNQueens(self, n):
        def dfs(row, sub):
            if row == n:
                res.append(sub)
            for i in range(n):
                if set(row, i):
                    board[row] = i
                    s = '.'*n
                    dfs(row+1,sub+[s[:i]+'Q'+s[i+1:]])
                    
        def set(index,num):
            for i in range(index):
                if board[i] == num or abs(num - board[i]) == index - i:
                    return False
            return True
                    
        board = [-1 for i in range(n)]
        res=[]
        dfs(0,[])
        return len(res)
