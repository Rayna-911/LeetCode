/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        RandomListNode dummy,tmp,p;
        HashMap<RandomListNode,RandomListNode> map = new HashMap<RandomListNode,RandomListNode>();
        dummy = new RandomListNode(0);
        tmp =dummy;
        
        if (head == null){
            return null;
        }
        while (head!=null){
            if(map.containsKey(head)){
                p = map.get(head);
            }
            else{
                p = new RandomListNode(head.label);
                map.put(head,p);
            }
            tmp.next = p;
            if(head.random!=null){
                if(map.containsKey(head.random)){
                    p.random = map.get(head.random);
                }else{
                    p.random = new RandomListNode(head.random.label);
                    map.put(head.random,p.random);
                }
            }
            tmp = p;
            head = head.next;
        }
        return dummy.next;
    }
}