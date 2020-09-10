package programmers;

public class Y2016 {
	public String getDayName(int a, int b) {
        String answer = "";
        String[] day = { "FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU" };
        int[] date = { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        int allDate = 0;
        for (int i = 0; i < a - 1; i++) {//if������ ���� ó�� ����. ��??
            allDate += date[i];
        }
        allDate += (b - 1);//���� ��¥�� (b-1)���� ����. ��??
        answer = day[allDate % 7];
        return answer;
    }

	
    public String solution(int a, int b) {
        String answer = "";
        String[] day = {"FRI","SAT","SUN","MON","TUE","WED","THU"};
        int[] date = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if (a==1){
            if(b%day.length>0){answer=day[b%day.length-1];}
            else{answer=day[day.length-1];}
            }
        else{
            int sum = 0;
            for (int i=1;i<a;i++){
                sum+=date[i-1];
            }
         if((b+sum)%day.length>0){answer=day[(b+sum)%day.length-1];}
            else{answer=day[day.length-1];}
        }
        return answer;
    }
}
