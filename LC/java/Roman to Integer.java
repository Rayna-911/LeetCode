public class Solution {
    public int romanToInt(String s) {
        int res;
        
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);
        
        res = map.get(s.charAt(s.length()-1));
        for (int t = s.length()-2; t >= 0; t--){
            if (map.get(s.charAt(t)) >= map.get(s.charAt(t+1))){
                res += map.get(s.charAt(t));
            }
            else{
                res -= map.get(s.charAt(t));
            }
        }
        return res;
    }
}