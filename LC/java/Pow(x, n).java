public class Solution {
    public double pow(double x, int n) {
        if(n==0){
            return 1;
        }
        
        if(n<0){
            double res = pow(x,-n-1);
            return 1/(res*x); // -214..8
        }
        else if(n%2==0){
            return pow(x*x,n/2);
        }
        else{
            return pow(x*x,n/2)*x;
        }
    }
}