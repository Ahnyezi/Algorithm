package programmers;

import java.util.ArrayList;
import java.util.List;
//���� ���ڴ� �Ⱦ�
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
	        List<Integer> list = new ArrayList<Integer>();//��̸���Ʈ ���
	        list.add(arr[0]);//�����Լ� add�� ���� ù��° �� ����

	        for (int i = 1; i < arr.length; i++) {
	            if (arr[i] != arr[i - 1]) //���ο� ��� �����Ҷ�����
	                list.add(arr[i]);//add�� �߰�  *idx �� �ʿ� ����
	        }

	        int[] answer = new int[list.size()];//�迭�� �����ؾ� �ϱ� ������ �迭�� �ű��

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
			int[] answer = new int[cnt]; //or new int [cnt+1] #cnt 0���� ī��Ʈ
			for (int i = 0; i < cnt; i++) { //i < cnt + 1 
				answer[i] = arr[idx[i]];
			}
	        return answer;
	    }


}
