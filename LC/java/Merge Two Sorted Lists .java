/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1==null){
            return l2;
        }
        if(l2==null){
            return l1;
        }
        
        ListNode dummy = new ListNode(0);
        ListNode tmp = dummy;
        
        while(l1 != null && l2 != null){
            if(l1.val < l2.val){
                tmp.next = l1;
                l1= l1.next;
                tmp = tmp.next;
            }    
            else{
                tmp.next = l2;
                l2= l2.next;
                tmp = tmp.next;
            }
        }
        
        if(l1 == null && l2 != null){
            tmp.next = l2;
        }
        if(l1 != null && l2 == null){
            tmp.next = l1;
        }
        
        return dummy.next;
    }
}