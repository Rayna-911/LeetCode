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
    public ListNode insertionSortList(ListNode head) {
        ListNode dummy,tmp,position;
        dummy = new ListNode(0);
        
        while(head != null){
            tmp = dummy;
            while(tmp.next!=null && head.val>tmp.next.val){
                tmp=tmp.next;
            }
            position = head.next;
            head.next = tmp.next;
            tmp.next = head;
            head = position;
        }
        
        return dummy.next;
    }
} 