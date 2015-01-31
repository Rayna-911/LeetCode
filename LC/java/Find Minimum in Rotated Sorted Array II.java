public class Solution {
    public int findMin(int[] num) {
        if(num.length==0){
            return -1;
        }
        
        if(num.length==1){
            return num[0];
        }
        
        if(num.length==2){
            return Math.min(num[0],num[1]);
        }
        
        int lo = 0;
        int hi = num.length-1;
        int mid = lo+(hi-lo)/2;
        
        if(num[lo]<num[hi]) return num[0];
        else if(num[lo]==num[hi]){
            if(num[mid]>num[lo]) return findMin(Arrays.copyOfRange(num,mid+1,num.length));
            else if(num[mid]<num[lo]) return findMin(Arrays.copyOfRange(num,0,mid+1));
            else return Math.min(findMin(Arrays.copyOfRange(num,0,mid+1)),findMin(Arrays.copyOfRange(num,mid+1,num.length)));
        }
        else{
            if(num[mid]>=num[lo]) return findMin(Arrays.copyOfRange(num,mid+1,num.length));
            else return findMin(Arrays.copyOfRange(num,0,mid+1));
        }
    }
}