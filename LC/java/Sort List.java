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
    public ListNode sortList(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        
        ListNode slow,fast,head1,head2;
        slow = fast = head1 = head;
        while(fast.next!=null && fast.next.next!=null){
            slow = slow.next;
            fast = fast.next.next;
        }
        
        head2 = slow.next;
        slow.next = null;
        
        head1 = sortList(head1);
        head2 = sortList(head2);
        head = merge(head1,head2);
        
        return head;
    }
    
    public ListNode merge(ListNode head1, ListNode head2){
        ListNode tmp = new ListNode(0);
        ListNode res = tmp;
        while(head1!=null && head2!=null){
            if(head1.val < head2.val){
                res.next = head1;
                head1 = head1.next;
                res = res.next;
            }
            else{
                res.next = head2;
                head2 = head2.next;
                res = res.next;
            }
        }
        
        if(head1==null){
            res.next = head2;
        }
        else{
            res.next = head1;
        }
        return tmp.next;
    }
   
}