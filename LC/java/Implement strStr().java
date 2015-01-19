public class Solution {
    public int strStr(String haystack, String needle) {
        int m = haystack.length(), n = needle.length();
        String sub;
        
        if(m<n){
            return -1;
        }
        else if(haystack.equals(needle)){
            return 0;
        }
        else if(n == 0) {
            return 0;
        }
        
        for(int i = 0; i< m-n+1; i++){
            sub = haystack.substring(i,i+n);
            if (sub.equals(needle)){
                return i;
            }
        }
        return -1;
        
    }
}