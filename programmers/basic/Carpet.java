package programmers;

public class Carpet {
	public int[] solution2(int brown, int yellow) {//판별식 사용
        int[] answer = new int[2];
        int x = (int)(brown + 4 + Math.sqrt((brown+4)*(brown+4) -16*(brown+yellow)))/4;
        int y = (brown + yellow)/x;
        answer[0]=Math.max(x,y); 
        answer[1]=Math.min(x,y);
        return answer;
    }

	 public int[] solution(int brown, int yellow) {
	        int[] answer = new int[2];
	        for(int i=3;i<=(int)Math.sqrt(brown+yellow);i++){
	            if((brown+yellow)%i==0){
	                int a = i;
	                int b = (brown+yellow)/i;
	                if(a+b-2==brown/2){
	                    answer[0]=b;
	                    answer[1]=a;
	                }
	            }
	        }
	        return answer;
	 }
}
