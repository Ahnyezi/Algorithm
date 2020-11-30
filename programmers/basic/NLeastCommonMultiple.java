package programmers;

import java.util.Arrays;

public class NLeastCommonMultiple {
	public int max(int s, int l){//�ִ����� �Լ�
        if(s>l){ //Math.max()/Math.min()�� ó�� ����
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
        int min = arr[0];//ù ������ �ּҰ������ �ڱ� �ڽ�
        for (int i=0;i<arr.length-1;i++){
            int max = max(min,arr[i+1]);//�� ���� �ִ�����
            min = min*arr[i+1]/max;//�� ���� �ּҰ����
        }
        return min; 
    }

}
