package programmers;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class FunctionDevel {
	public int[] solution(int[] progresses, int[] speeds) {
	      ArrayList<Integer> tmp = new ArrayList<Integer>();
	      int len = 0;
	      while(len<progresses.length){
	         int cnt = 0;
	         for(int i=0;i<progresses.length;i++){
	            if(progresses[i]<100){progresses[i]+=speeds[i];}
	         }
	         for(int i=len;i<progresses.length;i++){
	            if(progresses[i]<100){break;}cnt++;len++;}
	         if(cnt != 0){tmp.add(cnt);}
	      }
	      int[] res = new int[tmp.size()];
	      for (int i=0;i<tmp.size();i++){
	         res[i]=tmp.get(i);
	      }
	      return res;
	   }
	
	//다른 답안 (큐 사용) 더 느림
	public int[] solution2(int[] progresses, int[] speeds) {
        Queue<Integer> q = new LinkedList<>();
        List<Integer> answerList = new ArrayList<>();
        for (int i = 0; i < speeds.length; i++) {
            double remain = (100 - progresses[i]) / (double) speeds[i];
            int date = (int) Math.ceil(remain);//ceil:올림값
            if (!q.isEmpty() && q.peek() < date) {
                answerList.add(q.size());
                q.clear();
            }
            q.offer(date);
        }
        answerList.add(q.size());
        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = answerList.get(i);
        }
        return answer;
    }

}
