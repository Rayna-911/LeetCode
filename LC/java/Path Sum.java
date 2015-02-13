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
    public boolean hasPathSum(TreeNode root, int sum) {
        if(root==null) return false;
        
        return helper(root, 0, sum);
    }
    
    private boolean helper(TreeNode root, int curr, int sum){
        if(root==null) return false;
        
        if(root.left==null && root.right == null && curr+root.val == sum) return true;
        
        return helper(root.left, root.val+curr, sum) || helper(root.right,root.val+curr, sum);
    }
}