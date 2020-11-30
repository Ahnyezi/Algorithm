package programmers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class NoRemainArr {
	public int[] solution2(int[] arr, int divisor) {
        Arrays.sort(arr); //정렬 먼저!!
        List<Integer> lst1 = new ArrayList<Integer>();

        for(int item : arr) {
            if(item % divisor == 0) {
                lst1.add(item);
            }
        }

        int lstSize = lst1.size();
        if(lstSize == 0) {
            int[] answer = { -1 };
            return answer;
        }

        int[] answer = new int[lstSize];
        for(int i = 0; i < lstSize; ++i) {
            answer[i] = lst1.get(i);
        }
        return answer;
    }

	
	public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        int[] answer;
		for (int num: arr){
			if (num%divisor==0) 
                list.add(num);
		}
		if (list.size()<1) {
            answer = new int[]{-1};
            return answer;
        }
		else {
            answer = new int[list.size()];
            Collections.sort(list);
            for (int i=0;i<list.size();i++){
                answer[i]=list.get(i);
            }
            return answer;
        }
    }

}
