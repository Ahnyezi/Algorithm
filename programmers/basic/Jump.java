package programmers;

public class Jump {
	 public long solution(int n) {
		 int a = 1;
		 int b = 2;
		 
		 if(n==1){return a;}
		 else if(n==2){return b;}

		 for(int i=3;i<=n;i++){
			 int tmp = a;
			 a = b;
			 b = (tmp + b)%1234567;
		 }
		 return b;
	 }

}
