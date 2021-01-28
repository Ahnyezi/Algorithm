package algorithm.backtracking;
// 비숍

import java.util.Scanner;
import java.util.StringTokenizer;

public class b1799 {
    static int[][] board;
    static int N, cnt = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = Integer.parseInt(sc.nextLine());
        board = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(sc.nextLine());
            for (int j = 0; j < N; j++) {
                int num = Integer.parseInt(st.nextToken());
                board[i][j] = (num == 0) ? 1 : 0;// 반대로 넣기 (있으면 0, 없으면 1)
            }
        }
        dfs(0);
        System.out.println(cnt);
    }

    static void dfs(int col) {
        if (col == N) {
            cnt++;
            return;
        }

        for (int row = 0; row < N; row++) {
//            if (col != 0 && board[row][col] > 0) // ?? 몰겟다
            if (board[row][col] > 0)
                continue;

            // check
            int r1 = row, r2 = row;
            for (int nCol = col + 1; nCol < N; nCol++) {
                r1++; r2--;
                if (r1 < N)
                    board[r1][nCol] += 1;
                if (r2 >= 0)
                    board[r2][nCol] += 1;
            }
            for (int nCol = col + 1; nCol < N; nCol++){
                board[row][nCol] += 1;
            }

            dfs(col + 1);

            // unCheck
            r1 = row; r2 = row;
            for (int nCol = col + 1; nCol < N; nCol++) {
                r1++; r2--;
                if (r1 < N)
                    board[r1][nCol] -= 1;
                if (r2 >= 0)
                    board[r2][nCol] -= 1;
            }
            for (int nCol = col + 1; nCol < N; nCol++){
                board[row][nCol] -= 1;
            }
        }
    }
}
