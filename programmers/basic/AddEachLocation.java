package programmers;

public class AddEachLocation {
	public int solution2(int n) {
        int answer = 0;
        while(true){
            answer+=n%10; //1)10으로 나눈 나머지
            if(n<10)
                break;
            n=n/10; //2)10으로 나눈 몫으로 n초기화
        }
        return answer;
    }

	public int solution(int n) {
        int sum = 0;
        String str =Integer.toString(n); //int를 string으로 
		char[] num = str.toCharArray(); //string을 char배열로
		for(int i=0;i<num.length;i++){
			sum += num[i]-'0';
		}
        return sum;
    }

}
