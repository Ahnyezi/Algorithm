package programmers;

public class EvenOdd {
	public String evenOrOdd(int num) {
        return num % 2 == 0 ? "Even": "Odd";
    }

	public String solution(int num) {
        if(num%2==0){
            return new String("Even");//return "Even";
        } else{
            return new String("Odd");//return "Odd"; 이것도 가능!!
        }
    }

}
