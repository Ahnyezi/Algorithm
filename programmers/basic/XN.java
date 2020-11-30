package programmers;

import java.util.ArrayList;

//X만큼 간격이 있는 N개의 숫자
public class XN {
	public static long[] solution2(int x, int n) {
        long[] answer = new long[n];
        answer[0] = x;
        for (int i = 1; i < n; i++) {
            answer[i] = answer[i - 1] + x;
        }
        return answer;
    }

	public long[] solution(int x, int n) {
        long[] answer = new long[n];
    	ArrayList<Long> al = new ArrayList<Long>();
        for(int i=1;i<n+1;i++){
        	long res=(long)x*i;
        	al.add(res);
        }
        for(int i=0;i<n;i++){
        	answer[i]=al.get(i);
        }
        return answer;
    }

}
