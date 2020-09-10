package programmers;

public class SqrtInt {
	public long solution2(long n) {
	      if(n==1){
	          return 4;
	      }
	      for(long i=2;i<n;i++){//i가 n보다 작을 때까지 반복
	          if(n/i == i && n%i ==0){  //n을 x로 나누면 몫이 x으로 나누어 떨어질 경우. 
	              return (i+1)*(i+1);
	          }
	      }
	      return -1;
	  }

	public long solution(long n) {
        long i = 1;
        while (true) {
            if (n == i*i){
                return (i+1)*(i+1);
            }
            else if (i==n){
                return -1;
            }
            i++;
        }
    }
}
