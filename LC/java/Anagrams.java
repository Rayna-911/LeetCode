public class Solution {
    public ArrayList<String> anagrams(String[] strs) {
        HashMap<Integer, ArrayList<String>> map = new HashMap<Integer, ArrayList<String>>();
        ArrayList<String> res = new ArrayList<String>();
        
        if(strs.length==0){
            return res;
        }
        
        for (String s: strs){
            
            int[] cnt = new int[26];
            for(int i = 0; i<s.length();i++){
                cnt[s.charAt(i)-'a']++;
            }
            
            int h = hash(cnt);
            
            if(!map.containsKey(h)){
                map.put(h,new ArrayList<String>());
            }
            map.get(h).add(s);
        }
        
        for(ArrayList<String> v:map.values()){
            if(v.size()>1){
                res.addAll(v);
            }
        }
        return res;
    }
    
    public int hash(int[] cnt){
        int a = 31, b = 47, hash = 0;
        for (int i : cnt){
            hash = hash*a+i;
            a =a*b;
        }
        return hash;
    }
}