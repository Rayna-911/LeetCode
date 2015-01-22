public class Solution {
    public boolean exist(char[][] board, String word) {
        boolean res = false;
        
        for(int m = 0; m < board.length; m++){
            for(int n = 0; n<board[0].length; n++){
                res = res || dfs(m,n,0,board,word);
            }
        }
        return res;
    }

    public boolean dfs(int i, int j, int index, char[][] board, String word){
        if(i<0 || j<0 || i>=board.length || j>=board[0].length || board[i][j]!=word.charAt(index)){
            return false;
        }
        if(index == word.length()-1){
            return true;
        }
        board[i][j] = '#';
        
        boolean res = dfs(i+1,j,index+1,board,word) || dfs(i,j+1,index+1,board,word) || dfs(i-1,j,index+1,board,word) || dfs(i,j-1,index+1,board,word);
        
        board[i][j] = word.charAt(index);
        
        return res;
    }
}
