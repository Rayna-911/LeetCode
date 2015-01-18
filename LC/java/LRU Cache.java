public class LRUCache {
    class DoubleLL{
        DoubleLL prev;
        DoubleLL next;
        int key;
        int val;
        
        public DoubleLL(int key, int val){
            this.key = key;
            this.val = val;
            this.prev = null;
            this.next = null;
        }
    } 
    
    private int cap;
    private HashMap<Integer, DoubleLL> map = new HashMap<Integer, DoubleLL>();
    private DoubleLL head = new DoubleLL(-1,-1);
    private DoubleLL tail = new DoubleLL(-1,-1);
    
    public LRUCache(int capacity) {
        this.cap = capacity;  
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        if (map.containsKey(key)){
            move_to_tail(map.get(key));
            return map.get(key).val;
        }
        else{
            return -1;
        }
    }
    
    public void set(int key, int value) {
        if(map.containsKey(key)){
            DoubleLL node = map.get(key);
            node.val = value;
            move_to_tail(node);
        }
        else{
            if(map.size()==cap){
                //remove the first node
                DoubleLL first = head.next;
                head.next = first.next;
                first.next.prev = head;
                map.remove(first.key);
            }
            
            DoubleLL newNode = new DoubleLL(key,value);
            map.put(key,newNode);
            
            //add a new node to tail
                DoubleLL end = tail.prev;
                end.next = newNode;
                newNode.next = tail;
                tail.prev = newNode;
                newNode.prev = end;
        }
    }
    
    private void move_to_tail(DoubleLL node){
        if (node.next == tail){}
        else{
            node.prev.next = node.next;
            node.next.prev = node.prev;
        
            node.next = tail;
            node.prev = tail.prev;
            tail.prev.next = node;
            tail.prev = node;
        }
        
    }
}