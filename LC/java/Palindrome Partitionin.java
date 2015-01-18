import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
    
    public static ArrayList<ArrayList<String>> partition(String s) {
        ArrayList<ArrayList<String>> res = new ArrayList<ArrayList<String>>();
    	ArrayList<String> sub = new ArrayList<String>();
        dfs(s,sub,res);
        return res;
    }
    public static void dfs(String s, ArrayList<String> sub,ArrayList<ArrayList<String>> res){
        if(s.length() == 0){
            res.add(new ArrayList<String> (sub));
        }
        for(int i = 1; i < s.length()+1; i++){
            if(isPalindrome(s.substring(0, i))){
            	sub.add(s.substring(0,i));
                dfs(s.substring(i),sub,res);
                sub.remove(sub.size()-1);
            }
        }
    }
    public static boolean isPalindrome(String s){
        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) != s.charAt(s.length()-i-1)){
                return false;
            }
        }
        return true;
    }
}