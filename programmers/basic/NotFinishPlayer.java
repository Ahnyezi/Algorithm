package programmers;

import java.util.Arrays;

public class NotFinishPlayer {
	public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant); //string배열 sort.
        Arrays.sort(completion); //string배열 sort.
        int i;
        for ( i=0; i<completion.length; i++){
            if (!participant[i].equals(completion[i])){
                return participant[i];
            }
        }
        return participant[i]; //!!!
    }
}
