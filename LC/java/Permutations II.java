public class Solution {
    public ArrayList<ArrayList<Integer>> permuteUnique(int[] num) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        if(num.length==0){
            return res;
        }
        
        int[] visited = new int[num.length];
        ArrayList<Integer> sub = new ArrayList<Integer>();
        Arrays.sort(num);
        dfs(res,sub,num,visited);
        return res;
    }
    
    public void dfs(ArrayList<ArrayList<Integer>> res, ArrayList<Integer>sub, int[] num, int[] visited){
        if (sub.size()==num.length){
            res.add(new ArrayList<Integer>(sub));
            return;
        }
        
        for(int i = 0 ; i < num.length; i++){
            if(visited[i] == 1 || (i!=0 && num[i]==num[i-1] && visited[i-1]==0) ) continue;
            
            visited[i] = 1;
            sub.add(num[i]);
            dfs(res,sub,num,visited);
            sub.remove(sub.size()-1);
            visited[i] = 0;
            
        }
    }
}