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
    public ListNode reverseKGroup(ListNode head, int k) {
        if(head == null || k <= 1){
            return head;
        }
        ListNode start,end,h;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        start = dummy;
        h = head;
        int cnt = 0;
        
        while(h!=null){
            cnt += 1;
            end = h.next;
            if (cnt == k){
                start = reversePart(start,end);    
                cnt = 0;
            }
            h = end;
        }
        return dummy.next;
        
    }
    
    public ListNode reversePart(ListNode start, ListNode end){
        ListNode a,b,c;
        a = start.next;
        b = a.next;
        
        if (start == null || start.next == null){
            return start;
        }
        
        while(b != end){
            c = b.next;
            b.next = start.next;
            start.next = b;
            b = c;
        }
        a.next = end;
        return a;
    }
}