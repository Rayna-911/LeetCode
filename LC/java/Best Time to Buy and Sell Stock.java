public class Solution {
    public int maxProfit(int[] prices) {
        int minV = Integer.MAX_VALUE, maxV = Integer.MIN_VALUE;
        if (prices.length==0){
            return 0;
        }
        for (int i = 0; i < prices.length; i++){
            minV = Math.min(minV,prices[i]);
            maxV = Math.max(maxV,prices[i]-minV);
        }
        return maxV;
    }
}