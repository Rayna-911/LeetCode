/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ArrayList<ArrayList<Integer>> pathSum(TreeNode root, int sum) {
        ArrayList<Integer> sub = new ArrayList<Integer>();
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        
        if(root == null) return res;
        
        helper(root,sum,0,sub,res);
        return res;
    }
    
    private void helper(TreeNode root, int sum, int curr, ArrayList<Integer> sub, ArrayList<ArrayList<Integer>> res){
        if(root==null) return;
        
        if(root.left==null && root.right==null && curr+root.val == sum){
            sub.add(root.val);
            res.add(new ArrayList<Integer>(sub));
            sub.remove(sub.size()-1);
        }
        
        sub.add(root.val);
        helper(root.left, sum, root.val+curr, sub, res);
        helper(root.right, sum, root.val+curr, sub, res);
        sub.remove(sub.size()-1);
    }
}