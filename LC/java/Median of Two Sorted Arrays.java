public class Solution {
    public double findMedianSortedArrays(int A[], int B[]) {
        int m = A.length;
        int n = B.length;
        if ((m+n)%2 == 0){
            return (rec(A,B,(m+n)/2)+rec(A,B,(m+n)/2+1))*0.5;
        }
        else{
            return rec(A,B,(m+n)/2+1);
        }
    }
    
    public double rec(int A[], int B[], int k){
        int m = A.length;
        int n = B.length;
        if (m>n){
            return rec(B,A,k);
        }
        if (m == 0){
            return B[k-1];
        }
        if(k==1){
            return Math.min(A[0],B[0]);
        }
        
        int pa = Math.min(k/2,m);
        int pb = k-pa;
        
        if(A[pa-1]>B[pb-1]){
            return rec(A,Arrays.copyOfRange(B,pb,B.length),pa);
        }
        else{
            return rec(Arrays.copyOfRange(A,pa,A.length),B,pb);
        }
    }
}