package greedy;
import java.io.*;
import java.util.*;

public class n1931_2 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int cnt = Integer.parseInt(st.nextToken());
		
		ArrayList<Time> timeList = new ArrayList<Time>();
		for(int i=0;i<cnt;i++){
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			timeList.add(new Time(start,end));
		}
		System.out.println(timeList);
		
		Collections.sort(timeList);
		System.out.println("정렬 후:"+timeList);
		int result = 0;
		int prevEnd = 0;
		for(Time t:timeList){
			if(prevEnd<=t.getStart()){
				result+=1;
				prevEnd= t.getEnd();
			}
		}
		System.out.println("답:"+result);

		/*		
		<결과>
		[start:1, end:4, start:3, end:5, start:3, end:4, start:2, end:2, start:1, end:2]
		정렬 후:[start:1, end:2, start:2, end:2, start:1, end:4, start:3, end:4, start:3, end:5]
		답:3
		*/
	}
}

class Time implements Comparable<Time>{
	private int start;
	private int end;
	
	public Time(int start, int end){
		this.start = start;
		this.end = end;
	}

	public int getStart() {
		return start;
	}

	public void setStart(int start) {
		this.start = start;
	}

	public int getEnd() {
		return end;
	}

	public void setEnd(int end) {
		this.end = end;
	}

	@Override
	public int compareTo(Time t) {
		System.out.println();
		// TODO Auto-generated method stub
		if(this.end<t.getEnd()){
			return -1;
		}
		else if(this.end==t.getEnd()){
			if(this.start<t.getStart()){return -1;}
			else if(this.start==t.getStart()){return 0;}
			else{return 1;}
		}
		else{return 1;}
	}

	@Override
	public String toString() {
		return "start:" + start + ", end:" + end;
	}	
}
