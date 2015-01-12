public class Solution {
    
    public static int divide(int dividend, int divisor) {
	        
	        long a,b,sum,cnt,res = 0L;
	        int flag = 1;
	        
	        if((dividend<0&&divisor>0)||(dividend>0&&divisor<0)){
	            flag = -1;
	        }
	        
	        a = Math.abs((long)dividend);
	        b = Math.abs((long)divisor);
	        
	        
	        while(a>=b){
	            sum = b;
	            cnt = 1;
	            while(sum+sum<=a){
	                sum+=sum;
	                cnt+=cnt;
	                System.out.println(cnt);
	            }
	            a -= sum;
	            res += cnt;
	        }
	        
	        if(flag==-1){
	            res = 0-res;
	        }
	        if (res>Integer.MAX_VALUE){
	            res = Integer.MAX_VALUE;
	        }
	        if (res<Integer.MIN_VALUE){
	            res = Integer.MIN_VALUE;
	        }
	        return (int)res;
	    }
}