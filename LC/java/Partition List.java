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
    public ListNode partition(ListNode head, int x) {
        ListNode dummy,tmp,larger,l;
        dummy = new ListNode(0);
        larger = new ListNode(0);
        l = larger;
        tmp = dummy;
        
        while(head!=null){
            if(head.val<x){
                tmp.next = head;
                head=head.next;
                tmp = tmp.next;
                tmp.next = null;
                
            }
            else{
                larger.next = head;
                head = head.next;
                larger = larger.next;
                larger.next = null;
            }
        }
        tmp.next = l.next;
    
        return dummy.next;
            
    }
}