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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode p = dummy;
        
        if(n<=0){
            return null;
        }
        
        for(int i = 0; i < n; i++){
            if(head == null){
                return null;
            }
            head = head.next;
        }
        
        while(head!= null){
            head = head.next;
            p = p.next;
        }
        p.next = p.next.next;
        
        return dummy.next;
    }
}