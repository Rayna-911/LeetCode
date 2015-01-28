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
    public boolean isBalanced(TreeNode root) {
       
        int h = getHeight(root);
        if(h==-1){
            return false;
        }
        else{
            return true;
        }
    }
    
    private int getHeight(TreeNode x){
        if(x==null){
            return 0;
        }
        
        int l = getHeight(x.left);
        if(l==-1){
            return -1;
        }
        
        int r = getHeight(x.right);
        if(r==-1){
            return -1;
        }
        
        if(Math.abs(r-l)>1){
            return -1;
        }
        else{
            return 1+Math.max(l,r);
        }
    }
}