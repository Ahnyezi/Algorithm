package programmers;

public class SecretMap {
	public String[] solution2(int n, int[] arr1, int[] arr2) {
        String[] result = new String[n];
        for (int i = 0; i < n; i++) {
            result[i] = Integer.toBinaryString(arr1[i] | arr2[i]);//??
        }

        for (int i = 0; i < n; i++) {
            result[i] = String.format("%" + n + "s", result[i]);
            result[i] = result[i].replaceAll("1", "#");
            result[i] = result[i].replaceAll("0", " ");
        }

        return result;
    }
    public String[] solution(int n, int[] arr1, int[] arr2) {
        int[][] binary1 = new int[n][n];
        int[][] binary2 = new int[n][n];
        //arr1
        for(int i=0;i<arr1.length;i++){
            for (int j=arr1.length-1;j>=0;j--){
                binary1[i][j]=arr1[i]%2; 
                arr1[i]=arr1[i]/2;
            }
        }
        //arr2
        for(int i=0;i<arr2.length;i++){
            for (int j=arr2.length-1;j>=0;j--){
                binary2[i][j]=arr2[i]%2; 
                arr2[i]=arr2[i]/2;
            }
        }

        //연산
        int[][] tmp = new int[n][n];
        for(int i=0;i<binary1.length;i++){
            for (int j=0;j<binary1.length;j++){
                if(binary1[i][j]==1 || binary2[i][j]==1){tmp[i][j]=1;}
            }
        }
        //문자열로 리스트 반환
        String[] answer = new String[n];
        for(int i=0;i<tmp.length;i++){
            answer[i]="";
            for(int j=0;j<tmp.length;j++){
                if(tmp[i][j]==0){answer[i]+=" ";}
                else{answer[i]+="#";}
            }
        }
        return answer;
    }
}
