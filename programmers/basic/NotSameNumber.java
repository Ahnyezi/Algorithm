package programmers;

import java.util.ArrayList;
import java.util.List;
//같은 숫자는 싫어
public class NotSameNumber {
	public int[] solution3(int []arr) {
        ArrayList<Integer> tempList = new ArrayList<Integer>();
        int preNum = 10;
        for(int num : arr) {
            if(preNum != num)
                tempList.add(num);
            preNum = num;
        }       
        int[] answer = new int[tempList.size()];
        for(int i=0; i<answer.length; i++) {
            answer[i] = tempList.get(i);
        }
        return answer;
    }

	
	 public int[] solution2(int []arr) {
	        List<Integer> list = new ArrayList<Integer>();//어레이리스트 사용
	        list.add(arr[0]);//내장함수 add로 삽입 첫번째 값 삽입

	        for (int i = 1; i < arr.length; i++) {
	            if (arr[i] != arr[i - 1]) //새로운 요소 등장할때마다
	                list.add(arr[i]);//add로 추가  *idx 쓸 필요 없음
	        }

	        int[] answer = new int[list.size()];//배열로 리턴해야 하기 때문에 배열에 옮기기

	        for (int i = 0; i < list.size(); i++)
	            answer[i] = list.get(i);

	        return answer;
	    }

	
	 public int[] solution(int []arr) {
	        int cnt = 1; // or cnt= 0
			int[] idx = new int[arr.length];
			idx[0]=0;
			
			for (int i = 1; i < arr.length; i++) {
				if (arr[i - 1] != arr[i]) {
					cnt++;
					idx[cnt-1] = i; // or idx[cnt]=i
				}
			}
			int[] answer = new int[cnt]; //or new int [cnt+1] #cnt 0부터 카운트
			for (int i = 0; i < cnt; i++) { //i < cnt + 1 
				answer[i] = arr[idx[i]];
			}
	        return answer;
	    }


}
