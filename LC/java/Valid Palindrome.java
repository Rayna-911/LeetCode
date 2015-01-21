// public class Solution {
    // public boolean isPalindrome(String s) {
        // Stack<Character> stack = new Stack<Character>();
        
        // if(s.length()<2){
            // return true;
        // }
        
        // for(int i = 0; i<s.length(); i++){
            // if(Character.isDigit(s.charAt(i)) || Character.isLetter(s.charAt(i)))
                // stack.push(s.charAt(i));
        // }
        
        // if(stack.isEmpty())
            // return true;
        
        // int j=0;
        // while(j < s.length()){
            // if(Character.isDigit(s.charAt(j)) || Character.isLetter(s.charAt(j))){
                // char tmp = stack.pop();
                // if(Character.toLowerCase(tmp) != Character.toLowerCase(s.charAt(j))){
                    // return false;
                // }
            // }
            // j++;
        // }
        // return true;
    // }
// }

public class Solution {
    public boolean isPalindrome(String s) {
        if (s.length()<2){
            return true;
        }
        
        int f = 0, e = s.length()-1;
        
        while(f<e){
            while(f<s.length() && !(Character.isDigit(s.charAt(f)) || Character.isLetter(s.charAt(f)))){
                f++;
            }
            
            if (f>e){
                return true;
            }
            
            while(e>=0 && !(Character.isDigit(s.charAt(e)) || Character.isLetter(s.charAt(e)))){
                e--;
            }
            
            if(Character.toLowerCase(s.charAt(f)) != Character.toLowerCase(s.charAt(e))){
                return false;
            }
            else{
                f++;
                e--;
            }
        }
        return true;
    }
}