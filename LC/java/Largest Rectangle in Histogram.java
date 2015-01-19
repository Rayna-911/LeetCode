public class Solution {
    public int largestRectangleArea(int[] height) {
        Stack<Integer> s = new Stack<Integer>();
        int i = 0, tmp, area = 0, maxA = 0,com;//com is used to make sure that all items in stack will pop up finally
        
        while(i<height.length+1){
            if(i<height.length){
                com = height[i];
            }
            else{
                com = 0;
            }
            if (s.isEmpty() || height[s.peek()]<com){
                s.push(i);
                i++;
            }
            else{
                tmp = s.pop();
                if (s.isEmpty()){
                    area = height[tmp]*i;
                }
                else{
                    area = height[tmp]*(i-s.peek()-1);
                }
                maxA = Math.max(maxA,area);
            }
            
        }
        return maxA;
    }
}