package programmers;
//���￡�� �輭�� ã��
public class FindKim {

}
class Kim {
    public String solution(String[] seoul) {
        String answer = "";
        String target = "Kim";
        for (int i=0;i<=1000;i++){
        	boolean flag=target.equals(seoul[i]);
        	if (flag==true){
        		answer+="�輭���� "+i+"�� �ִ�";
        		break;
        	}
        }  
        return answer;
    }
}
