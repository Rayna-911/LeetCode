public class Solution {
    public int longestValidParentheses(String s) {
        int tmp  = -1, maxlen = 0;
        Stack<Integer> q = new Stack<Integer>();
        
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '('){
                q.add(i);
            }
            else{
                if(q.size()==0){
                    tmp = i;
                }
                else{
                    q.pop();
                    if(q.size()==0){
                        maxlen = Math.max(maxlen, i-tmp);
                    }
                    else{
                        maxlen = Math.max(maxlen, i-q.get(q.size()-1));
                    }
                }
            }
        }
        return maxlen;
    }
}
