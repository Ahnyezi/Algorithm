package programmers;

public class IntegerSum {}
// �� ������ ��
class Solution {//���콺�� ����

    public long solution(int a, int b) {
        return sumAtoB(Math.min(a, b), Math.max(b, a));//tip1
    }

    private long sumAtoB(long a, long b) {
        return (b - a + 1) * (a + b) / 2;//a����b���� ���ڰ���/�ΰ��� ��/2
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


