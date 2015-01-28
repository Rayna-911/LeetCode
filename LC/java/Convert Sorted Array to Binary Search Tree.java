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
    public TreeNode sortedArrayToBST(int[] num) {
        return helper(num,0,num.length-1);
    }
    
    public TreeNode helper(int[] arr, int start, int end){
        if(start>end){
            return null;
        }
        
        int mid = (start+end)/2;
        TreeNode root = new TreeNode(arr[mid]);
        root.left = helper(arr,start,mid-1);
        root.right = helper(arr,mid+1,end);
        
        return root;
    }
}