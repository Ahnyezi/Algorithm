package programmers;

public class Harshad {
	public boolean isHarshad(int num){
	    String[] temp = String.valueOf(num).split("");//string�迭 ó��
	    int sum = 0;
	    for (String s : temp) {
	        sum += Integer.parseInt(s);//�� ���ڿ� int�� ĳ�����ؼ� ���
	    }
	    if (num % sum == 0) {
	            return true;
	    } else {
	      return false;
	    }
	}

	public boolean solution(int x) {
		int sum = 0;
		int tmp = x;
		while (true) {
			sum += tmp % 10;
			tmp = tmp / 10;
			if (tmp < 1)
				break;
		}
		if (x % sum == 0)
			return true;
		else
			return false;
    }

}
