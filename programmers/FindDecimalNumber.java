package programmers;

public class FindDecimalNumber {
	 public int solution(int n) {
	       int answer = 0;
	        int[] nums = new int[n+1];
	        for (int i=2;i<=n;i++){
	            nums[i]=i;
	        }
	        for(int i=2;i<=n;i++){
	            if(nums[i]==0){continue;}//이미 소수의 배수로 체크된 숫자면 pass(현재 수보다 작은 수의 배수라면, 현재 수의 배수도 이미 check되었음)
	            for(int j=i*2;j<=n;j+=i){//소수가 아니면 check(0 할당)
										//j<n(x) j<=n(o)
										//j*=i(등비가 i인 수), j+=i(i의 배수)
	                nums[j]=0;
	            }
	        }
	        for(int i=2;i<=n;i++){
	            if(nums[i]!=0){answer++;}
	        }
	        return answer;
	    }

}
