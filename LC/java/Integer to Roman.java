public class Solution {
    public String intToRoman(int num) {
        int[] nums = {1,4,5,9,10,40,50,90,100,400,500,900,1000};
        String[] str = {"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};
        String res = "";
        
        for(int i = nums.length-1; i>-1; i--){
            while(num>=nums[i]){
                res += str[i];
                num -= nums[i];
            }
        }
        return res;
    }
}