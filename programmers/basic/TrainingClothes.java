package programmers;

import java.util.HashMap;

public class TrainingClothes {
	 public int solution2(int n, int[] lost, int[] reserve) {
       
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer> ();
        int answer = 0;
        for(int i = 1; i <= n; i++) {
            map.put(i,0);
        }
        for(int student : reserve) {
            map.put(student,map.get(student)+1);
        }
        for(int student : lost) {
            map.put(student,map.get(student)-1);
        }   
        for(int i = 1; i<= n; i++) {
            if(map.get(i) == -1 ) {
            	//map.containsKey(0) == null 이므로 예외처리
                if(map.containsKey(i-1) && map.get(i-1) ==1 ) {
                    map.put(i,0);
                    map.put(i-1,0);
                }
                //map.containsKey(n+1) == null 이므로 예외처리
                else if(map.containsKey(i+1) && map.get(i+1) == 1) {
                      map.put(i,0);
                      map.put(i+1,0);
                }
            }
        }
        for(int i = 1; i <= n; i++) {
           if(map.get(i) != -1) answer++;
        }
        return answer;
    }

	
	 public int solution(int n, int[] lost, int[] reserve) {
        int cnt = 0;
        int[] stu = new int[n + 1];
        for (int i = 0; i < lost.length; i++) {// 잃어버린 학생 방 = -1
            stu[lost[i]]--;
        }
        for (int i = 0; i < reserve.length; i++) {// 여벌 있는 학생 방  = 1
            stu[reserve[i]]++;
        }
        for (int i=1;i<stu.length-1;i++){
            if(stu[i]==-1){
                if(stu[i-1]==1){		//다른 방법: {stu[i-1]=stu[i]=0;}
                    stu[i-1]--;		// 왼쪽 두 개의 변수를 모두 0으로 초기화
                    stu[i]++;
                    }
                else if(stu[i+1]==1){	//다른 방법: {stu[i+1]=stu[i]=0;}
                    stu[i+1]--;
                    stu[i]++;
                    }
            }
        }
        for(int i=1;i<stu.length;i++){
            if(stu[i]!=-1){cnt++;}
        }
        return cnt;
    }

}
