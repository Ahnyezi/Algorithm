package programmers;

import java.util.Stack;

public class SteelStick {
	public int solution2(String arrangement) {//스택 사용
	       int answer = 0;
	       Stack<Character> stick = new Stack<Character>();

	       for(int i=0;i<arrangement.length();i++){
	           char ch = arrangement.charAt(i);
	           if(ch=='('){stick.push(ch);}
	           else{
	               stick.pop();
	               if(arrangement.charAt(i-1)=='('){answer+=stick.size();}
	               else{answer+=1;}
	           }
	       }
	       return answer;
	   }

	
	public int solution(String arrangement) {
        int answer = 0;
        int stick = 0;
        char prev = ' ';
        for(int i=0;i<arrangement.length();i++){
            if(arrangement.charAt(i)=='('){stick++;prev='(';}
            else{
                if(prev=='('){stick--;answer+=stick;}
                else{stick--;answer+=1;}
                prev=')';
            }
        }
        return answer;
    }

}
