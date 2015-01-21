public class Solution {
    public int sqrt(int x) {
        long l = 0, r = x;
        
        while(l<=r){
            long mid = l+(r-l)/2;
            if(mid*mid > x){
                r=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        return (int)r;
    }
}