public class Solution {
    public String longestPalindrome(String s) {
        if(s.length()<2){
            return s;
        }
        int[] res = {0,0};
        for(int i = 0; i<s.length(); i++){
            int[] x = getPalindrome(s,i,i);
            if((x[1]-x[0])>(res[1]-res[0])){
                res[0] = x[0]; 
                res[1] = x[1];
            }
            
            int[] y = getPalindrome(s,i,i+1);
            if((y[1]-y[0])>(res[1]-res[0])){
                res[0] = y[0]; 
                res[1] = y[1];
            }
        }
        return s.substring(res[0],res[1]);
    }
    
    public int[] getPalindrome(String s, int lo, int hi){
        while(lo>=0 && hi<s.length() && s.charAt(lo) == s.charAt(hi)){
            lo--;
            hi++;
        }
        int[] x = new int[2];
        x[0] = lo+1;
        x[1] = hi;
        return x;
    }
}