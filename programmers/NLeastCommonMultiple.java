package programmers;

import java.util.Arrays;

public class NLeastCommonMultiple {
	public int max(int s, int l){//최대공약수 함수
        if(s>l){ //Math.max()/Math.min()로 처리 가능
            int tmp=s;
            s=l;
            l=tmp;
        }
        while(true){
            int tmp = l%s;
            if(tmp==0){return s;}
            else{l=s; s=tmp;}
        }
    }

    public int solution(int[] arr) {       
        Arrays.sort(arr);   
        int min = arr[0];//첫 시행의 최소공배수는 자기 자신
        for (int i=0;i<arr.length-1;i++){
            int max = max(min,arr[i+1]);//두 수의 최대공약수
            min = min*arr[i+1]/max;//두 수의 최소공배수
        }
        return min; 
    }

}
