public class Solution {
    public int removeElement(int[] A, int elem) {
        int f = 0, e = A.length-1;
        if(A.length==0){
            return 0;
        }
        
        while(f<=e){
            if(A[f]==elem){
                A[f] = A[e];
                e--;
            }
            else{
                f++;
            }
        }
        return e+1;
    }
}