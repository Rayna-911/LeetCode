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
    public boolean isSymmetric(TreeNode root) {
        if(root==null) return true;
        
        else if(root.left == null && root.right == null) return true;
        
        else if(root.left != null && root.right != null) return helper(root.left,root.right);
        
        else return false;
    }
    
    private boolean helper(TreeNode x, TreeNode y){
        if(x==null && y== null) return true;
        
        else if (x!=null && y!= null) return x.val == y.val && helper(x.left, y.right) && helper(x.right, y.left);
        
        else return false;
        
        
    }
} 