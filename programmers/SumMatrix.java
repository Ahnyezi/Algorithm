package programmers;

public class SumMatrix {
	public int[][] sumMatrix(int[][] A, int[][] B) {
	    int row = Math.max(A.length, B.length); //��:
	    int col = Math.max(A[0].length, B[0].length); //��
	        //Math.max(a,b) �� ���� ���� �� ū ���� ����? �ʿ��
	    int[][] answer = new int[row][col];
	    for(int i=0; i<row ; i++){
	      for(int j=0; j<col; j++){
	        answer[i][j] = A[i][j] + B[i][j];
	      }
	    }
	        return answer;
	}
	
	 public int[][] solution(int[][] arr1, int[][] arr2) {
         int[][] answer = new int[arr1.length][arr1[0].length];
        for (int i=0;i<arr1.length;i++){
        	for(int j=0;j<arr1[0].length;j++){
        		answer[i][j]=arr1[i][j]+arr2[i][j];
        	}
        }
        return answer;
    }

}
