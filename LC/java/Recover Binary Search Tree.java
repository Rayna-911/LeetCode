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
    private TreeNode p1,p2,pre;
    
    public void recoverTree(TreeNode root) {
        find(root);
        int tmp;
        tmp = p1.val;
        p1.val = p2.val;
        p2.val = tmp;
    }
    
    public void find(TreeNode root){
        if(root != null){
            find(root.left);
            if (pre!=null && root.val<pre.val){
                p1 = root;
                if (p2 == null){
                p2 = pre;
                }
            }
            pre = root;
            find(root.right);
        }
    }
}