package programmers;

public class CaesarCipher {
	public String solution2(String s, int n) {
        String answer="";
        char start=' ';
        char[] str = s.toCharArray();
        for(char alpha:str){
            if (alpha != ' '){
                start = Character.isLowerCase(alpha)? 'a':'A';
                alpha = (char)(start + (alpha+n-start)%26);
            }
            answer += alpha;
        }
        return answer;
    }

	public String solution(String s, int n) {
	  String answer="";
	  char[] str = s.toCharArray();
	  for(char alpha:str){
	  	int tmp =0;
	  char tmp2 = ' ';
	  	if(Character.isUpperCase(alpha)){tmp = alpha+n<91 ? alpha+n : alpha+n-26;}
	  	else if(Character.isLowerCase(alpha)){tmp = alpha+n<123 ? alpha+n : alpha+n-26;}
	  	else{answer += alpha;} //alpha(x) tmp(o)
	              tmp2= (char)tmp;
	              answer += tmp2;
	  		}
	          return answer;
	      }

}
