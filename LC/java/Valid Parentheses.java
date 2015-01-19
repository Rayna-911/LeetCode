public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        char tmp;
        for(int i = 0; i < s.length(); i++){
            if (s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{'){
                stack.push(s.charAt(i));
            }
            else{
                if(stack.isEmpty()){
                    return false;
                }
                tmp = stack.pop();
                if ((tmp == '(' && s.charAt(i) == ')') || (tmp == '[' && s.charAt(i) == ']') || (tmp == '{' && s.charAt(i) == '}')) ;
                else{
                    return false;
                }
            }
        }
        if(stack.isEmpty()){
            return true;
        }
        else{
            return false;
        }
    }
}