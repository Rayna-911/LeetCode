public class Solution {
    public ArrayList<ArrayList<Integer>> permute(int[] num) {
        
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> sub = new ArrayList<Integer>();
        
        if (num.length == 0){
            return res;
        }
        
        dfs(res,sub,num);
        return res;
    }
    
    public void dfs(ArrayList<ArrayList<Integer>> res, ArrayList<Integer> sub, int[] num){
        if(sub.size()==num.length){
            res.add(new ArrayList<Integer>(sub));
            return;
        }
        
        for(int i = 0; i<num.length; i++){
            if(sub.contains(num[i])){
                continue;
            }
            sub.add(num[i]);
            dfs(res,sub,num);
            sub.remove(sub.size()-1);
        }
        
    }
}