/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
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
    
    private ListNode curr;
    
    public TreeNode sortedListToBST(ListNode head) {
        int size;
        TreeNode root;
        
        size = getLen(head);
        curr = head;
        root = res(size);
        
        return root;
    }
    
    public int getLen(ListNode head){
        int size = 0;
            
        while(head!=null){
            size += 1;
            head = head.next;
        }
        return size;
    }
    
    public TreeNode res(int size){
        TreeNode root,left,right;
        
        if (size<=0){
            return null;
        }
        
        left = res(size/2);
        root = new TreeNode(curr.val);
        curr = curr.next;
        right = res(size - size/2 -1);
        
        root.left = left;
        root.right = right;
        return root;
    } 
}