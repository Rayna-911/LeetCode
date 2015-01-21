public class Solution {
    public ArrayList<String> generateParenthesis(int n) {
        if(n<=0){
            return new ArrayList<String>();
        }
        ArrayList<String> res = new ArrayList<String>();
        dfs(res,"",n,n);
        return res;
    }
    
    public void dfs(ArrayList<String> res, String sub, int left, int right){
        if(left<0 || right<0 || left>right){
            return;
        }
        
        if(left==0 && right==0){
            res.add(sub);
            return;
        }
        
        dfs(res,sub+"(",left-1,right);
        dfs(res,sub+")",left,right-1);
        
    }
}