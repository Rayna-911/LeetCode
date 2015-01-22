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
    public int sumNumbers(TreeNode root) {
        if(root==null){
            return 0;
        }
        
        return dfs(root,0);
    }
    
    public int dfs(TreeNode n,int sum){
        if(n == null){
            return 0;
        }
        sum = sum*10+n.val;
        
        if(n.left==null && n.right==null){
            return sum;
        }
        
        return dfs(n.left,sum)+dfs(n.right,sum);
    }
}