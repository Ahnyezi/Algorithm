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
		while (k > 1) {//����
			int b = 0;
			// k���� ���� �� ��,���� ū a�� ã��
			for (i = n - 1; i >= 0; i--) {
				if (a[i] < k) {
					b = a[i];
					break;//�������;� ��. �ƴϸ� ���� ���� ������ �ʱ�ȭ
				}
			}
			System.out.println("���� ���� ��ġ:"+b);
			// ���õ� b�� ���� ���� cnt��, �������� k�� ����
			cnt += k / b;
			System.out.println("������� ����� ���� ����:"+cnt);
			k %= b;
			System.out.println("������:"+k);
			System.out.println();
		}
		System.out.println("�� ��� ����:"+cnt);
		sc.close();
	}
}
// ���� ����
// N(���� ����), K(��ġ�� ��)
// A[]: �� ������ ��ġ. ��������.
// �� ���� ���� ������ ���? �� �ʿ�?
// K�� ����� �� �ʿ��� ���� ������ �ּҰ�

// �ǻ��ڵ�
