package programmers;

import java.util.Arrays;

public class MaxMin {
	public String getMinMaxString(String str) {
        String[] tmp = str.split(" ");
        int min, max, n;
        min = max = Integer.parseInt(tmp[0]);
        for (int i = 1; i < tmp.length; i++) {//check2(선택정렬st)
                n = Integer.parseInt(tmp[i]);
            if(min > n) min = n;
            if(max < n) max = n;
        }
        return min + " " + max;//check1
    }

	 public String solution(String s) {
         String answer = "";
        String [] str=s.split(" ");
        int[] nums=new int[str.length];
        for(int i=0;i<nums.length;i++) {
            nums[i]=Integer.parseInt(str[i]);
        }
        Arrays.sort(nums);
            answer+=nums[0]+" "+nums[nums.length-1];
         return answer;
     }

}
