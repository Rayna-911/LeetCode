public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        int[] res = new int[2];
        
        for (int i = 0; i<numbers.length; i++){
            if (map.containsKey(target - numbers[i])){
                res[0] = map.get(target - numbers[i])+1;
                res[1] = i+1;
                return res;
            }
            else{
                map.put(numbers[i],i);
            }
        }
        res[0] = 0;
        res[1] = 0;
        return res;
    }
}