package programmers;
// ����� ��
public class MeasureSum {
    public int solution(int n) {
        int answer = 0;
        
        for (int j=n;j>0;j--){
        	if(n%j==0){
        		answer+=j;
        	}
        }
        return answer;
    }
}
