package programmers;
//수박수박수박수박수박수?
public class WaterMelon {
    public String watermelon(int n){
    String result = "";
    for (int i = 0; i < n; i++)
      result += i % 2 == 0 ? "수" : "박";
        return result;
    }
}
class WaterMelon2 {
    public String solution(int n) {
        String answer = "";        
        char ch1 ='수';
        String ch2 ="수박";
        
        if (n==1){
            answer+=ch1;
        } else if(n>=2){
            if (n%2==0){
                for(int i=1;i<=n/2;i++){
                    answer+=ch2;
                }
            } else{
                for(int i=1;i<=n/2;i++){
                    answer+=ch2;
                }answer+=ch1;
            }
        }
        return answer;
    }
}
