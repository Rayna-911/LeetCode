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
    public ListNode deleteDuplicates(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        
        ListNode dummy,tmp,p;
        int val;
        dummy = new ListNode(0);
        dummy.next = head;
        tmp = dummy;
        
        while(tmp.next!=null && tmp.next.next!=null){
            if(tmp.next.val == tmp.next.next.val){
                val = tmp.next.next.val;
                while(tmp.next!=null && tmp.next.val==val){
                    tmp.next = tmp.next.next;   
                    }
            }else{
                tmp = tmp.next;
            }
        }
        return dummy.next;
    }
}