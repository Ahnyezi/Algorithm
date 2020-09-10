package programmers;

public class IntegerSum {}
// 두 정수의 합
class Solution {//가우스의 덧셈

    public long solution(int a, int b) {
        return sumAtoB(Math.min(a, b), Math.max(b, a));//tip1
    }

    private long sumAtoB(long a, long b) {
        return (b - a + 1) * (a + b) / 2;//a부터b까지 숫자개수/두개의 합/2
    }
}
class Solution2 {
    public long solution(int a, int b) {
        long answer = 0;
        if (a>b){
            for(int i=b;i<=a;i++){
                answer+=i;
            }
        }else if(a<b){
            for(int i=a;i<=b;i++){
                answer+=i;
            }
        }else{
            answer= a;
        }
        return answer;
    }
}


