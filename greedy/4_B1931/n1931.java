package greedy;
import java.util.*;
import java.io.*;

public class n1931 {
	public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(tokenizer.nextToken());
        
		int i = 0, max = 0, cnt = 0;
		Map<Integer,String> time = new HashMap<Integer,String>();
		
		for(i=0;i<n;i++){
			tokenizer = new StringTokenizer(br.readLine(),"\n");//default는 " "
			String t = tokenizer.nextToken();
			String[] str = t.split(" ");
			
			if(max<Integer.parseInt(str[1])) max= Integer.parseInt(str[1]);
			time.put(Integer.parseInt(str[1])-Integer.parseInt(str[0]),t);
			if(i==n-1){System.out.println(Integer.parseInt(str[1])+"/"+Integer.parseInt(str[0]));}
		}
		System.out.println();

		
        Object[] mapkey = time.keySet().toArray();
		Arrays.sort(mapkey);
		
		int[] room = new int[max+1];
		
		String tmp = time.get("5 7");//아예 안들어갓어
		System.out.println(tmp);//null값 왜지
		
		for(Integer nKey : time.keySet()){
			System.out.println(nKey+"/"+time.get(nKey));
			System.out.println(cnt+"번째");
			boolean flag = true;
			String[] str = time.get(nKey).split(" ");

			// 시작시간과 끝시간 같을 경우
			if(str[0].equals(str[1])){
				System.out.println("check1");
				if(room[Integer.parseInt(str[0])]<2){
					room[Integer.parseInt(str[0])]++;
					cnt++;
				}
				System.out.println("cnt:"+cnt);
				continue;
			}
			System.out.println("check2");
			for(i=Integer.parseInt(str[0]);i<=Integer.parseInt(str[1]);i++){
				if(room[i]>1){flag=false; break;}
			}
			if(flag){
				cnt++;
				for(i=Integer.parseInt(str[0]);i<=Integer.parseInt(str[1]);i++){
					room[i]++;
				}
			}
			System.out.println("cnt:"+cnt);
		}
		
        bw.write(String.valueOf(cnt));

        br.close();
        bw.close();
		
//		Scanner sc = new Scanner(System.in);
//		
//		int n = Integer.parseInt(sc.nextLine()),i = 0, max = 0, cnt = 0;
//		//Map 선언
//		Map<Integer,String> time = new HashMap<Integer,String>();
//		
//		for(i=0;i<n;i++){
//			String t = sc.nextLine();
//			String[] str=t.split(" ");
//			
//			//*max 선언해두고  value값 중 가장 작은 값, 큰값으로 초기화
//			if(max<Integer.parseInt(str[1])) max= Integer.parseInt(str[1]);
//			//끝시간 -시작시간(key),시간 정보(value) 
//			for(int j=0;j<str.length;j++){
//				time.put(Integer.parseInt(str[1])-Integer.parseInt(str[0]),t);
//			}
//		}
//		//key array로 변환해서 sort
//		Object[] mapkey = time.keySet().toArray();
//		Arrays.sort(mapkey);
//		
//		//max개의 방을 가진 list 생성 (0,1이면 삽입가능. 2이면 삽입 불가)
//		int[] room = new int[max+1];///////오류 수정 new int[max]
//		
//		//map의 앞에서부터 뽑아와서 list방에 연산
//		for(Integer nKey : time.keySet()){
//			boolean flag = true;
//			String[] str = time.get(nKey).split(" ");
//
//			//넣을 수 있는지 확인
//			if(str[0].equals(str[1])){
//				if(room[Integer.parseInt(str[0])]<2){
//					room[Integer.parseInt(str[0])]++;
//					cnt++;
//				}
//				continue;
//			}
//			for(i=Integer.parseInt(str[0]);i<=Integer.parseInt(str[1]);i++){
//				if(room[i]>1){flag=false; break;}
//			}
//			//넣을 수 있다면, 삽입
//			if(flag){
//				cnt++;
//				for(i=Integer.parseInt(str[0]);i<=Integer.parseInt(str[1]);i++){
//					room[i]++;
//				}
//			}
//		}
//		
//		//결과 보기
//		System.out.println(cnt);
        
        
        //1차시도 x: map에서 key 중복 x
	}
}

//문제 이해
//n개의 회의가 있음
//회의 시간을 겹치지 않게 하면서
//최대한 많은 회의가 회의실을 사용할 수 있게하라

//의사코드

//Map 선언
//시간 정보(value) *max 선언해두고  value값 중 가장 작은 값, 큰값으로 초기화
//끝시간 -시작시간(key)
//key array로 변환
//sort

//max개의 방을 가진 list 생성 (0,1이면 삽입가능. 2이면 삽입 불가)

//map의 앞에서부터 뽑아와서 list방에 연산

