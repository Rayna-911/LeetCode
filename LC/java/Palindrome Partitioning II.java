public class Solution {
    public int minCut(String s) {
        if (s.length() <2){
            return 0;
        }
        
        int[] dp = new int[s.length()+1];
        boolean[][] table = lookup(s);
        
        for(int i = 0; i < s.length()+1; i++){
            dp[i] = s.length()-i;
        }
        
        for (int i = s.length()-1;i>-1; i--){
            for(int j = i; j < s.length(); j++){
                if (s.charAt(i) == s.charAt(j) && (j-i<=2||table[i+1][j-1]==true)){
                    dp[i] = Math.min(1+dp[j+1],dp[i]);
                }
            }
        }
        return dp[0]-1;
    }
    
    private boolean[][] lookup(String s){
        boolean[][] table = new boolean[s.length()][s.length()];
        for(int i = 0; i < s.length(); i++){
            table[i][i]=true;
        }
        
        for(int i = 0; i < s.length()-1;i++){
            table[i][i+1] = (s.charAt(i)==s.charAt(i+1));
        }
        
        for(int len = 2; len<s.length(); len++){
            for(int m = 0; m+len < s.length(); m++){
                table[m][m+len] = (s.charAt(m)==s.charAt(m+len) && (len<=2||table[m+1][m+len-1]==true));
            }
        }
        return table;
    }
    
    
}