package greedy;

import java.util.*;

public class n11047 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int i = 0, n = 10, k = 4790,
				a[] = new int[]{1,5,10,50,100,500,1000,5000,10000,50000};
//		int i = 0, n = sc.nextInt(), k = sc.nextInt(), a[] = new int[n];
//		for (i = 0; i < n; i++) {
//			a[i] = sc.nextInt();
//		}

		int cnt = 0;
		while (k > 1) {//오류
			int b = 0;
			// k보다 작은 수 중,가장 큰 a값 찾기
			for (i = n - 1; i >= 0; i--) {
				if (a[i] < k) {
					b = a[i];
					break;//빠져나와야 함. 아니면 제일 작은 값으로 초기화
				}
			}
			System.out.println("나눌 동전 가치:"+b);
			// 선택된 b로 나눈 몫을 cnt에, 나머지를 k에 삽입
			cnt += k / b;
			System.out.println("현재까지 사용한 동전 개수:"+cnt);
			k %= b;
			System.out.println("나머지:"+k);
			System.out.println();
		}
		System.out.println("총 사용 개수:"+cnt);
		sc.close();
	}
}
// 문제 이해
// N(동전 종류), K(가치의 합)
// A[]: 각 동전의 가치. 오름차순.
// 각 방의 수는 전방의 배수? 왜 필요?
// K원 만드는 데 필요한 동전 개수의 최소값

// 의사코드
