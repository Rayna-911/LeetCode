/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode reorderList(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        
        ListNode res,slow,fast,head2,a,b,tmp,r,p1,p2;
        res = head;
        slow = head;
        fast = head;
        
        while(fast.next!=null && fast.next.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        head2 = slow.next;
        slow.next = null;
        
        //reverse the second part
        a = head2;
        b = head2.next;
        head2.next = null;
        while(b!=null){
            tmp = b;
            b = b.next;
            tmp.next = a;
            a = tmp;
        }
        head2 = a;
     
        //merge
        while(head!=null && head2!=null){
            p1 = head.next;
            head.next = head2;
            p2 = head2.next;
            head2.next = p1;
            head = p1;
            head2 = p2;
        }
        
        if (head != null){
            head.next = null;
        }
        return res;
    }
}