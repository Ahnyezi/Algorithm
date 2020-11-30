package programmers;

public class RemovePhonenumber {
	public String solution2(String phone_number) {
	     char[] ch = phone_number.toCharArray();
	     for(int i = 0; i < ch.length - 4; i ++){
	         ch[i] = '*';
	     }
	     return String.valueOf(ch);
	  }

	 public String solution(String phone_number) {
        char[] arr = phone_number.toCharArray();
		int cnt = 0;
		for (int i=arr.length-1;i>=0;i--){
			cnt++;
			if(cnt>4){
				arr[i]='*';
			}
		}
        return (new String(arr));
    }
}
