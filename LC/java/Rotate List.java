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
    public ListNode rotateRight(ListNode head, int n) {
        if (head == null || head.next == null){
            return head;
        }
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode p = dummy;
        int cnt = 0, step;
        
        while(p.next!=null){
            p = p.next;
            cnt += 1;
        }
        
        p.next = dummy.next;
        
        step = cnt - (n % cnt);
        while(step > 0){
            p = p.next;
            step -= 1;
        }
        
        head = p.next;
        p.next = null;
        
        return head;
    }
}