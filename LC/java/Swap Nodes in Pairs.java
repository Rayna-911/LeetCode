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
    public ListNode swapPairs(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode tmp = dummy;
        ListNode p;
        
        while(tmp.next!=null && tmp.next.next!=null){
            p = tmp.next.next;
            tmp.next.next = p.next;
            p.next = tmp.next;
            tmp.next = p;
            tmp=tmp.next.next;
        }
        return dummy.next;
    }
}