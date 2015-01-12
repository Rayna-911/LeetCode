public class Solution {
    public int[] plusOne(int[] digits) {
        int flag = 1,tmp;
        
        for(int i = digits.length-1; i >= 0; i--){
            tmp = digits[i]+flag;
            digits[i] = tmp % 10;
            flag = tmp / 10;
        }
        
        if(flag != 0){
            int[] res = new int[digits.length+1];
            res[0] = flag;
            for(int i = 0; i < digits.length; i++){
                res[i+1] = digits[i];
            }
            return res;
        }
        return digits;
    }
}