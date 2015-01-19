public class Solution {
    public int atoi(String str) {
        if (str == null || str.length() < 1) {
			return 0;
		}
		str=str.trim();
		
		char flag = '+';
		int i = 0;
		if (str.charAt(0) == '+'){
		    i++;
		}
		else if (str.charAt(0) == '-'){
		    i++;
		    flag = '-';
		}
		
		double res = 0;
		while (str.length()>i && str.charAt(i) <='9' && str.charAt(i)>='0'){
			res = res*10 + (str.charAt(i)-'0');
			i++;
		}
		
		if (flag == '-'){
			res = -res;
		}
		
		if (res > Integer.MAX_VALUE){
			return Integer.MAX_VALUE;}
		else if (res < Integer.MIN_VALUE){
			return Integer.MIN_VALUE;}
		else{return (int)res;}
		
    }
}