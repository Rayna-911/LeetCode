class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        def bfs(x,y):
            if board[x][y] == 'O':
                q.append((x,y))
                fill(x,y)
            while q:
                tmp = q.pop(0)
                i = tmp[0]
                j = tmp[1]
                fill(i+1,j)
                fill(i-1,j)
                fill(i,j+1)
                fill(i,j-1)
                
        def fill(i,j):
            if i > m-1 or j > n-1 or i < 0 or j < 0 or board[i][j]  != 'O':
                return
            q.append((i,j))
            board[i][j] = 'v'
            
        m = len(board)
        if m < 3:
            return 
        n = len(board[0])
        q = []
        
        for i in range(m):
            bfs(i,0)
            bfs(i,n-1)
        for i in range(n):
            bfs(0,i)
            bfs(m-1,i)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'v':
                    board[i][j] ='O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                
