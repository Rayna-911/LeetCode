public class Solution {
    public String addBinary(String a, String b) {
        
        String res = "";
        int tmp = 0;
        
        for(int i = 0; i < Integer.max(a.length(),b.length()); i++){
            if(i<a.length() && a.charAt(a.length()-1-i) == '1'){
                tmp += 1;
            }
            if(i<b.length() && b.charAt(b.length()-1-i) == '1'){
                tmp += 1;
            }
            res = (tmp%2) + res;
            tmp = tmp / 2;
        }
        if(tmp!=0){
            res = "1" + res;
        }
        return res;
    }
}