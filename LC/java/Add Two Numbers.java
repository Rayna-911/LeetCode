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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy, tmp;
        int flag = 0;
        
        dummy = new ListNode(0);
        tmp = dummy;
        
        if(l1==null){
            return l2;
        }
        if(l2==null){
            return l1;
        }
        
        while(l1!=null && l2!=null){
            tmp.next = new ListNode((l1.val+l2.val+flag)%10);
            flag = (l1.val+l2.val+flag)/10;
            tmp = tmp.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        
        if(l1==null){
            while(l2!=null){
                tmp.next = new ListNode((l2.val+flag)%10);
                flag = (l2.val+flag)/10;
                tmp = tmp.next;
                l2 = l2.next;
            }
        }
        
        if(l2==null){
            while(l1!=null){
                tmp.next = new ListNode((l1.val+flag)%10);
                flag = (l1.val+flag)/10;
                tmp = tmp.next;
                l1 = l1.next;
            }
        }
        
        if(flag!=0){
            tmp.next = new ListNode(flag);
            tmp = tmp.next;
        }
        
        tmp.next = null;
        
        return dummy.next;
    }
}