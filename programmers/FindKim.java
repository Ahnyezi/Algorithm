package programmers;
//서울에서 김서방 찾기
public class FindKim {

}
class Kim {
    public String solution(String[] seoul) {
        String answer = "";
        String target = "Kim";
        for (int i=0;i<=1000;i++){
        	boolean flag=target.equals(seoul[i]);
        	if (flag==true){
        		answer+="김서방은 "+i+"에 있다";
        		break;
        	}
        }  
        return answer;
    }
}
