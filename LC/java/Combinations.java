public class Solution {
    public ArrayList<ArrayList<Integer>> combine(int n, int k) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> sub = new ArrayList<Integer>();
        
        dfs(res,sub,n,k,1);
        
        return res;
    }
    
    public void dfs(ArrayList<ArrayList<Integer>> res,ArrayList<Integer> sub,int n, int k, int start){
        if(sub.size()==k){
            res.add(new ArrayList<Integer>(sub));
            return;
        }
        
        for(int i = start; i<n+1; i++){
            sub.add(i);
            
            dfs(res,sub,n,k,i+1);
            sub.remove(sub.size()-1);
        }
    }
}