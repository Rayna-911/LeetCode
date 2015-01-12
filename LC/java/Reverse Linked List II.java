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
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if(head==null || m>=n){
            return head;
        }
        
        ListNode p, mp, a, b, temp;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        p = dummy;
        
        for(int i = 1; i < m; i++){
            if(p == null){
                return null;
            }
            p = p.next;
        }
        
        mp = a = p.next;
        b = a.next;
        for(int i = m; i < n; i++){
            if(b == null){
                return null;
            }
            temp = b.next;
            b.next = a;
            a = b;
            b = temp;
        }
        mp.next = b;
        p.next = a;
        
        return dummy.next;
        
    }         
}