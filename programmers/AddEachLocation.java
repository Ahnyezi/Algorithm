package programmers;

public class AddEachLocation {
	public int solution2(int n) {
        int answer = 0;
        while(true){
            answer+=n%10; //1)10���� ���� ������
            if(n<10)
                break;
            n=n/10; //2)10���� ���� ������ n�ʱ�ȭ
        }
        return answer;
    }

	public int solution(int n) {
        int sum = 0;
        String str =Integer.toString(n); //int�� string���� 
		char[] num = str.toCharArray(); //string�� char�迭��
		for(int i=0;i<num.length;i++){
			sum += num[i]-'0';
		}
        return sum;
    }

}
