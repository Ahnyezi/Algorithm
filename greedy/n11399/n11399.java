package greedy;

import java.util.*;
public class n11399 {//16m
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int i=0, n = sc.nextInt(), p[] = new int[n];
		for(i=0;i<n;i++)p[i] = sc.nextInt();
		
		Arrays.sort(p);
		int add = 0, sum = 0;
		for (i = 0; i < p.length; i++) {
			add += p[i];
			sum += add;
		}
		System.out.println(sum);
		sc.close();
	}
}
