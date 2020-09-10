package programmers;

import java.util.Arrays;

public class NumberK {
	public int[] solution2(int[] array, int[][] commands) {//copy
        int[] answer = new int[commands.length];

        for(int i=0; i<commands.length; i++){
            int[] temp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            Arrays.sort(temp);
            answer[i] = temp[commands[i][2]-1];
        }
        return answer;
    }

	public static int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int index = 0 ;
        for(int i = 0 ; i < commands.length ; i++)
        {
            int start = commands[i][0];
            int end = commands[i][1];
            int k = commands[i][2];
            int[] tmp = new int[end - start + 1];
            int a = 0;
            for(int j = start - 1 ; j < end ; j++)
                tmp[a++] = array[j];
            Arrays.sort(tmp);
            answer[index++] = tmp[k-1];
        }
        return answer;
    }

}
