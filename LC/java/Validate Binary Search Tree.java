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
    private boolean first = true;
    private int last = Integer.MIN_VALUE;
    public boolean isValidBST(TreeNode root) {
       
       if(root == null){
           return true;
       } 
       
       if(!isValidBST(root.left)){
           return false;
       }
       
       if(!first && last>=root.val)
       {
           return false;
       }
       
       first = false;
       last = root.val;
       
       if(!isValidBST(root.right)){
           return false;
       }
       return true;
    }
}