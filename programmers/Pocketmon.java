package programmers;

import java.util.Arrays;
import java.util.HashSet;

public class Pocketmon {
	 public int solution2(int[] nums) {//�ؽ������� ����Ž��
         HashSet<Integer> hs = new HashSet<>();
         for(int i =0; i<nums.length;i++) {
             hs.add(nums[i]);//��� �迭 ���� ��� ADD
         }
         if(hs.size()>nums.length/2)
             return nums.length/2;
         return hs.size();
 }

	public int solution(int[] nums) {
        Arrays.sort(nums);
		int prev = nums[0];
		int cnt = 1;
		for(int i=1;i<nums.length;i++){
			if (prev!=nums[i]){cnt++;prev=nums[i];}
		 }
        if (cnt>nums.length/2){return nums.length/2;}//�� ��츸 ����
       return cnt;
    }

}
