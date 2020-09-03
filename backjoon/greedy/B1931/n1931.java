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
			tokenizer = new StringTokenizer(br.readLine(),"\n");//default�� " "
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
		
		String tmp = time.get("5 7");//�ƿ� �ȵ���
		System.out.println(tmp);//null�� ����
		
		for(Integer nKey : time.keySet()){
			System.out.println(nKey+"/"+time.get(nKey));
			System.out.println(cnt+"��°");
			boolean flag = true;
			String[] str = time.get(nKey).split(" ");

			// ���۽ð��� ���ð� ���� ���
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
//		//Map ����
//		Map<Integer,String> time = new HashMap<Integer,String>();
//		
//		for(i=0;i<n;i++){
//			String t = sc.nextLine();
//			String[] str=t.split(" ");
//			
//			//*max �����صΰ�  value�� �� ���� ���� ��, ū������ �ʱ�ȭ
//			if(max<Integer.parseInt(str[1])) max= Integer.parseInt(str[1]);
//			//���ð� -���۽ð�(key),�ð� ����(value) 
//			for(int j=0;j<str.length;j++){
//				time.put(Integer.parseInt(str[1])-Integer.parseInt(str[0]),t);
//			}
//		}
//		//key array�� ��ȯ�ؼ� sort
//		Object[] mapkey = time.keySet().toArray();
//		Arrays.sort(mapkey);
//		
//		//max���� ���� ���� list ���� (0,1�̸� ���԰���. 2�̸� ���� �Ұ�)
//		int[] room = new int[max+1];///////���� ���� new int[max]
//		
//		//map�� �տ������� �̾ƿͼ� list�濡 ����
//		for(Integer nKey : time.keySet()){
//			boolean flag = true;
//			String[] str = time.get(nKey).split(" ");
//
//			//���� �� �ִ��� Ȯ��
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
//			//���� �� �ִٸ�, ����
//			if(flag){
//				cnt++;
//				for(i=Integer.parseInt(str[0]);i<=Integer.parseInt(str[1]);i++){
//					room[i]++;
//				}
//			}
//		}
//		
//		//��� ����
//		System.out.println(cnt);
        
        
        //1���õ� x: map���� key �ߺ� x
	}
}

//���� ����
//n���� ȸ�ǰ� ����
//ȸ�� �ð��� ��ġ�� �ʰ� �ϸ鼭
//�ִ��� ���� ȸ�ǰ� ȸ�ǽ��� ����� �� �ְ��϶�

//�ǻ��ڵ�

//Map ����
//�ð� ����(value) *max �����صΰ�  value�� �� ���� ���� ��, ū������ �ʱ�ȭ
//���ð� -���۽ð�(key)
//key array�� ��ȯ
//sort

//max���� ���� ���� list ���� (0,1�̸� ���԰���. 2�̸� ���� �Ұ�)

//map�� �տ������� �̾ƿͼ� list�濡 ����

