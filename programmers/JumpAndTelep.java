package programmers;

public class JumpAndTelep {
	 public int solution2(int n) {
	        int cnt = 0;
	    	while(n>0){//���� 0���� Ŭ ���� ����
	            if (n%2!=0){cnt++;n-=1;}//1�� ��� ���� �� �ʿ����.
	            n/=2;//¦Ȧ �Ѵ� �ʿ��� ������ �������� �α�
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
