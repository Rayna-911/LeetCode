public class Solution {
    public int reverse(int x) {
        char flag;
        long res=0;
        if(x>= 0){
            flag = '+';
        }
        else{
            flag = '-';
            x = -1*x;
        }
        
        while (x != 0) {
        res = res*10 + x%10;
        x = x/10;
        }
        
        if (flag == '-'){
            res = -1*res;
        }
        
        if (res > Integer.MAX_VALUE || res < Integer.MIN_VALUE ) {
            return 0;
        }
        else {
        return (int)res;
            
        }
    }
}