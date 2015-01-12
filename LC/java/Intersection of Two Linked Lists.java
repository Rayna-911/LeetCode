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
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode p1,p2;
        int a=1,b=1;
        
        if(headA==null || headB==null){
            return null;
        }
        
        p1 = headA;
        while(p1.next!=null){
            p1 = p1.next;
            a += 1;
        }
        
        p2 = headB;
        while(p2.next!=null){
            p2 = p2.next;
            b += 1;
        }
        
        if(p1!=p2){
            return null;
        }
        
        if(a>b){
            for(int i = 0; i<a-b; i++){
                headA = headA.next;
            }
        }
        
        if(a<b){
            for(int i = 0; i<b-a; i++){
                headB = headB.next;
            }
        }
        
        while(headA!=null){
            if(headA == headB){
                return headA;
            }
            else{
                headA = headA.next;
                headB = headB.next;
            }
        }
        return null;
    }
}