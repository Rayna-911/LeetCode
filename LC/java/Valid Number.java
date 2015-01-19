public class Solution {
    public boolean isNumber(String s) {
        int i = 0, e = s.length()-1;
        
        //delete the space around the string
        while(i<=e && Character.isWhitespace(s.charAt(i))){ 
            i++;  
        }
        if (i>e){ 
            return false; 
        }
        while(e>=i && Character.isWhitespace(s.charAt(e))){ 
            e--;
        }
        
        // ignore the sign
        if(s.charAt(i)=='+' || s.charAt(i)=='-'){ i++; }
        
        boolean num = false;
        boolean dot = false;
        boolean exp = false;
        
        while(i<=e){
            char curr = s.charAt(i);
            if(Character.isDigit(curr)){
                num = true;
            }
            else if(curr == '.'){
                if(dot || exp){
                    return false;
                }
                dot = true;
            }
            else if(curr == 'e'){
                if(exp || num == false){
                    return false;
                }
                exp = true;
                num = false;
            }
            else if(curr == '+' || curr == '-'){
                if(s.charAt(i-1)!='e'){
                    return false;
                }
            }
            else{
                return false;
            }
            i++;
        }
        return num;
    }
}