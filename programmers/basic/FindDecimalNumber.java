package programmers;

public class FindDecimalNumber {
	 public int solution(int n) {
	       int answer = 0;
	        int[] nums = new int[n+1];
	        for (int i=2;i<=n;i++){
	            nums[i]=i;
	        }
	        for(int i=2;i<=n;i++){
	            if(nums[i]==0){continue;}//�̹� �Ҽ��� ����� üũ�� ���ڸ� pass(���� ������ ���� ���� ������, ���� ���� ����� �̹� check�Ǿ���)
	            for(int j=i*2;j<=n;j+=i){//�Ҽ��� �ƴϸ� check(0 �Ҵ�)
										//j<n(x) j<=n(o)
										//j*=i(��� i�� ��), j+=i(i�� ���)
	                nums[j]=0;
	            }
	        }
	        for(int i=2;i<=n;i++){
	            if(nums[i]!=0){answer++;}
	        }
	        return answer;
	    }

}
