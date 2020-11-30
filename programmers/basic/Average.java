package programmers;

public class Average {
	 public double solution(int[] arr) {
	        double sum = 0;
		        for(int i: arr){
		        sum+=i;
		    }
		    return sum/arr.length; //굳이 변수에 안담아줘도 됌!!
	    }
}
