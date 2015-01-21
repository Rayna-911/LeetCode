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
    public ListNode mergeKLists(ArrayList<ListNode> lists) {
        if(lists==null || lists.size()==0){
            return null;
        }
        
        Queue<ListNode> heap = new PriorityQueue<ListNode>(lists.size(), new Comparator<ListNode>(){
            public int compare(ListNode a, ListNode b){
                return a.val>b.val?1:(a.val==b.val?0:-1);
            }});
        for(ListNode l: lists){
            if(l!=null){
                heap.add(l);
            }
        }
        
        ListNode dummy = new ListNode(0), tmp = dummy,curr;
        
        while(!heap.isEmpty()){
            curr = heap.poll();
            tmp.next = curr;
            tmp = curr;
            if(curr.next!=null){
                heap.add(curr.next);
            }
        }
        return dummy.next;
        
    }
}