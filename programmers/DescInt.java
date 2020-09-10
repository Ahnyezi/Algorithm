package programmers;

import java.util.Arrays;

public class DescInt {
	public int reverseInt(int n){
        String arr[]=String.valueOf(n).split("");
	    Arrays.sort(arr);
	    String str = "";
	    for(int i=arr.length-1; i>=0; i--){
	         str+= arr[i];
	    }
	    return Integer.parseInt(str);
	}

	public long solution(long n) {
        String number = "";
        number += n;
		char[] numbers = number.toCharArray();
		int[] nums = new int[number.length()];
        
        		for (int i=0;i<number.length();i++){
			nums[i] = numbers[i]-'0'; //오류1: (int)numbers[i];
		}
		number = "";
		
		for (int i=0;i<nums.length;i++){//오류2: i<nums.length-1로 마지막 방 안넣음
			int max = i;
			for(int j =i+1;j<nums.length;j++){
				if(nums[max]<nums[j]){
					max=j;
				}
			}
			if (i != max){
				int tmp=nums[max];
				nums[max]=nums[i];
				nums[i]=tmp;	
			}
			number+=nums[i];//여기서 i로 삽입하기 때문
		}
        return Long.parseLong(number);
	}
}
