package programmers;

public class ReverseArr {
	 public int[] solution2(long n) {
	      String a = "" + n; //숫자 한줄로 string으로 만들기!!!
	        int[] answer = new int[a.length()];
	        int cnt=0;

	        while(n>0) {//n이 정수일 때까지 반복
	            answer[cnt]=(int)(n%10);//마지막 숫자 첫째 방에 넣기.
	            n/=10; //n을 10으로 나눈 몫을 다시 n에 집어넣기
	            System.out.println(n);
	            cnt++;//방 칸 수 늘리기
	        }
	      return answer;
	  }

	 public int[] solution(long n) {
	        char[] arr = String.valueOf(n).toCharArray();//stringbuilder의 reverse()사용 가능
			int[] answer = new int[arr.length];
	        
	        for(int i=0;i<arr.length;i++){
				answer[arr.length-1-i]=arr[i]-'0';
			}
	        return answer;
	    }
}
