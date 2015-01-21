// public class Solution {
    // public void merge(int A[], int m, int B[], int n) {
        // if(m==0){
            // for(int y = 0; y<n;y++){
                // A[y] = B[y];
            // }
        // }
        // else if(n==0){
            // return;
        // }
        
        // int i=0,j=0,k=0;
        // int[] res = new int[m+n];
        
        // while(i<m && j<n){
            // if(A[i]<=B[j]){
                // res[k] = A[i];
                // i++;
            // }
            // else{
                // res[k] = B[j];
                // j++;
            // }
            // k++;
        // }
        
        // if(i==m){
            // while(j<n){
                // res[k] = B[j];
                // k++;
                // j++;
            // }
        // }
        
        // else if(j==n){
            // while(i<m){
                // res[k] = A[i];
                // k++;
                // i++;
            // }
        // }
        // for(int x = 0; x<res.length;x++){
                // A[x] = res[x];
            // }
        
    // }
// }




public class Solution {
    public void merge(int A[], int m, int B[], int n) {
        
        int index = m+n;
        
        while(m>0 && n>0){
            if(A[m-1]>B[n-1]){
                A[--index] = A[--m];
            }
            else{
                A[--index] = B[--n];
            }
        }
        
        while(n>0){
            A[--index] = B[--n];
        }
        
    }
}