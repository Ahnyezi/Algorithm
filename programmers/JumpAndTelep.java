package programmers;

public class JumpAndTelep {
	 public int solution2(int n) {
	        int cnt = 0;
	    	while(n>0){//조건 0보다 클 경우로 변경
	            if (n%2!=0){cnt++;n-=1;}//1의 경우 따로 둘 필요없음.
	            n/=2;//짝홀 둘다 필요한 연산은 공통으로 두기
	    	}
	    	return cnt;
	    }

	public int solution(int n) {
        int cnt = 0;
        while(true){
            if(n==1){cnt++;break;}
            if(n%2==0){n=n/2;} 
            else if(n%2!=0){cnt++;n=(n-1)/2;}
        }
        return cnt;
    }

}
