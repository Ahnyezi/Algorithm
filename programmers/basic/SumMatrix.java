package programmers;

public class SumMatrix {
	public int[][] sumMatrix(int[][] A, int[][] B) {
	    int row = Math.max(A.length, B.length); //행:
	    int col = Math.max(A[0].length, B[0].length); //열
	        //Math.max(a,b) 두 개의 인자 중 큰 값을 리턴? 필요없
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
