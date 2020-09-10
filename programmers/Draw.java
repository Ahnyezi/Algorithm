package programmers;

public class Draw {
	public int solution(int n, int a, int b){
        int answer = 0;
       while(Math.max(a, b)-Math.min(a, b)>=1){
           a = (a%2==1)? a/2+1 :a/2;
           b = (b%2==1)? b/2+1 :b/2;      
           answer++;
       }
       return answer;
  }

}
