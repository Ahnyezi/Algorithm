package greedy;

import java.util.*;

class bag {
	public int solution(int n) {
		// n이 3의 배수
		if (n % 3 == 0) {
			return n / 3;
		}
		// n이 5의 배수
		else if (n % 5 == 0) {
			return n / 5;
		}
		// n이 15의 배수
		else if (n % 15 == 0) {
			int num = n / 5;
			num += (n % 5) / 3;
			return num;
		}
		return -1;
	}
}

public class n2839 {// 1h 19m
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int cnt = 0, answer = 0, n = sc.nextInt();

		while (n % 5 != 0 && n > 0) {
			n -= 3;
			cnt++;
		}
		answer = (n < 0) ? -1 : n / 5 + cnt;
		System.out.println(answer);
		sc.close();
	}
}
