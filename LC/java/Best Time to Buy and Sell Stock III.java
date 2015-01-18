public class Solution {
    public int maxProfit(int[] prices) {
        int maxP;
        int[] f = new int[prices.length];
        int minV;
        int[] b = new int[prices.length];
        int maxV;
        
        if(prices.length == 0){
            return 0;
        }
        minV = prices[0];
        maxP = Integer.MIN_VALUE;
        for(int i = 0; i < prices.length; i++){
            minV = Math.min(minV,prices[i]);
            maxP = Math.max(maxP,prices[i]-minV);
            f[i] = maxP;
        }
        maxV = prices[prices.length-1];
        maxP = Integer.MIN_VALUE;
        for(int i = prices.length-1; i>-1; i--){
            maxV = Math.max(maxV,prices[i]);
            maxP = Math.max(maxP,maxV-prices[i]);
            b[i] = maxP;
        }
        maxP = f[f.length-1];
        for (int i = 0; i < prices.length-1; i++){
            maxP = Math.max(maxP, f[i]+b[i+1]);
        }
        return maxP;
    }
}