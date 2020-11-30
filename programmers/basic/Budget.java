package programmers;

import java.util.Arrays;

public class Budget {
	public int solution(int[] d, int budget) {
      int sum = 0;
        int cnt = 0;
        Arrays.sort(d);
        for(int i=0; i<d.length; i++) {
            if(budget < sum + d[i]) {break;}
            else {
                sum += d[i];
                cnt++;
            }
        }
        return cnt;
  }
}
