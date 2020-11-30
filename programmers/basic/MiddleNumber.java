package programmers;
//같은 숫자는 싫어
class StringExercise{
    String getMiddle(String word){
        return word.substring((word.length()-1) / 2, word.length()/2 + 1);    
    }

public class MiddleNumber {
    public String solution(String s) {
        String answer = "";
    	char[] str = s.toCharArray();
    	int len =str.length;
    	if(len%2==0){
    		answer+=str[len/2-1];
    		answer+=str[len/2];
    	} else {
    		answer+=str[len/2];
    	}
        return answer;
    	}
	}
}