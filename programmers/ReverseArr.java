package programmers;

public class ReverseArr {
	 public int[] solution2(long n) {
	      String a = "" + n; //���� ���ٷ� string���� �����!!!
	        int[] answer = new int[a.length()];
	        int cnt=0;

	        while(n>0) {//n�� ������ ������ �ݺ�
	            answer[cnt]=(int)(n%10);//������ ���� ù° �濡 �ֱ�.
	            n/=10; //n�� 10���� ���� ���� �ٽ� n�� ����ֱ�
	            System.out.println(n);
	            cnt++;//�� ĭ �� �ø���
	        }
	      return answer;
	  }

	 public int[] solution(long n) {
	        char[] arr = String.valueOf(n).toCharArray();//stringbuilder�� reverse()��� ����
			int[] answer = new int[arr.length];
	        
	        for(int i=0;i<arr.length;i++){
				answer[arr.length-1-i]=arr[i]-'0';
			}
	        return answer;
	    }
}
