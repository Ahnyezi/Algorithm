package programmers;

public class Fibonacci {
	public int solution(int n) {
    int a = 1;
	int b = 1;
	for(int i=3;i<=n;i++){
		int tmp = b;
		b = (a+b)%1234567;
		a= tmp;
	}
	return b;
	}
}
