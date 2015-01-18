public class Solution {
    public int maxProfit(int[] prices) {
        int maxP = 0;
        
        if(prices.length==0){
            return 0;
        }
        
        for(int i = 0; i<prices.length-1; i++){
            maxP += Math.max(0,prices[i+1]-prices[i]);
        }
        return maxP;
    }
}