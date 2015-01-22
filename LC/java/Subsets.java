public class Solution {
    public ArrayList<ArrayList<Integer>> subsets(int[] S) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> sub = new ArrayList<Integer>();
        
        Arrays.sort(S);
        dfs(res,sub,S,0);
        return res;
    }
    
    public void dfs(ArrayList<ArrayList<Integer>> res,ArrayList<Integer> sub,int[] S,int start){
        res.add(new ArrayList<Integer>(sub));
        
        for(int i = start; i<S.length; i++){
            sub.add(S[i]);
            dfs(res,sub,S,i+1);
            sub.remove(sub.size()-1);
        }
    }
}