public class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> s = new Stack<Integer>();
        String op = "+-*/";
        
        
        for(String i:tokens){
            if(!op.contains(i)){
                s.push(Integer.valueOf(i));
            }
            else{
                if(s.size()<2){
                    return -1;
                }
                int a = s.pop();
                int b = s.pop();
                if(i.equals("+")){
                    s.push(a+b);
                }
                else if(i.equals("-")){
                    s.push(b-a);
                }
                else if(i.equals("*")){
                    s.push(a*b);
                }
                else{
                    s.push(b/a);
                }
            }
        }
        
        return s.pop();
    } 
}