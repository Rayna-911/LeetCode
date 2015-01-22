public class Solution {
    public int numDecodings(String s) {
        if(s.length()==0 || s.charAt(0)=='0'){
            return 0;
        }
        int[] res = new int[s.length()+1];
        res[0]=1;
        res[1]=1;
        
        for(int i = 2; i <res.length; i++){
            if(Integer.parseInt(s.substring(i-2,i))>10 && Integer.parseInt(s.substring(i-2,i))<27 && s.charAt(i-1) !='0'){
                res[i] = res[i-1]+res[i-2];
            }
            else if(Integer.parseInt(s.substring(i-2,i))==10 || Integer.parseInt(s.substring(i-2,i))==20){
                res[i] = res[i-2];
            }
            else if(s.charAt(i-1) !='0'){
                res[i] = res[i-1];
            }
            else return 0;
        }
        return res[res.length-1];
    }
}