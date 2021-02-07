package algorithm.simulation;
// 책 페이지

import java.io.*;

public class b1019 {

    public static void main(String[] args) throws IOException {
        solution();
    }

    static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int[] count = new int[10];

//        int A = 1;
        int digit = 1;
        while (A <= B) {

            // B % 10의 마지막자리를 9로 만들기 이전의 값들을
            // count 배열에 넣는다.
            while (B % 10 != 9 && A <= B) {
                calc(B, count, digit);
//                while (B > 0){
//                    count[B % 10] += digit;
//                    B /= 10;
//                }
                B--;
            }
            if (B < A) break;

            // A % 10의 마지막자리를 0으로 만들기 이전의 값들을
            // count 배열에 넣는다
            while (A % 10 != 0 && A <= B) {
                calc(A, count, digit);
//                while (A > 0){
//                    count[A % 10] += digit;
//                    A /= 10;
//                }
                A++;
            }

            B /= 10;
            A /= 10;

            for (int i = 0; i < 10; i++) {
                count[i] += (B - A + 1) * digit;
            }
            digit *= 10;
        }

        for (int c : count) {
            sb.append(c).append(" ");
        }
        System.out.println(sb);
    }

    static void calc(int x, int[] count, int digit) {
        while (x > 0) {
            count[x % 10] += digit;
            x /= 10;
        }
    }
}
