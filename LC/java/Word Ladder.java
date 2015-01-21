public class Solution {
    public int ladderLength(String start, String end, Set<String> dict) {
        if(dict == null || dict.size()==0){
            return 0;
        }
        Queue<String> q = new LinkedList<String>();
        q.add(start);
        dict.remove(start);
        
        int res=1;
        
        while(!q.isEmpty()){
            int size = q.size();
            for(int i = 0; i<size;i++){
                String tmp = q.poll();
                for(char c ='a'; c<='z';c++){
                    for(int j = 0; j<tmp.length();j++){
                        if(c==tmp.charAt(j)){
                            continue;
                        }
                        String t = replace(tmp,j,c);
                        if(t.equals(end)){
                            return res+1;
                        }
                        if(dict.contains(t)){
                            dict.remove(t);
                            q.add(t);
                        }
                    }
                }
            }
            res++;
        }
        return 0;
    }
    
    public String replace(String s, int i, char a){
        char[] c = s.toCharArray();
        c[i] = a;
        return new String(c);
    }
}