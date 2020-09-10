package programmers;

import java.util.Stack;

class Solutiont {
    class Tower {
        int idx;
        int height;
        public Tower(int idx, int height) {
            this.idx = idx;
            this.height = height;
        }
    }
    public int[] solution(int[] heights) {
        Stack<Tower> st = new Stack<>();//tower 타입의 스택 생성
        int[] answer = new int[heights.length];
        for (int i = 0; i < heights.length; i++) {
            Tower tower = new Tower(i + 1, heights[i]);//idx,height
            int receiveIdx = 0;
            while (!st.isEmpty()) {
                Tower top = st.peek();
                if (top.height > tower.height) {
                    receiveIdx = top.idx;
                    break;
                }
                st.pop();
            }
            st.push(tower);
            answer[i] = receiveIdx;
        }
        return answer;
    }
}


public class Tower {
	 public int[] solution(int[] heights) {
	        int[] answer = new int[heights.length];
	        for (int i=answer.length-1; i>0; i--) {
	            for (int j=i-1; j>=0; j--) {
	                if(heights[i]<heights[j]){
	                    answer[i] = j+1;
	                    break;
	                }
	            }
	        }
	        return answer;
	    }

}
