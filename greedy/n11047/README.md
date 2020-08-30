# 문제11047 | 동전 0

## 문제<br/>
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.<br/>
<br/>
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.<br/>

#### 입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)<br/>
<br/>
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
<br/><br/>

#### 출력
첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.<br/>
<br/>

#### 입출력 예제
![image](https://user-images.githubusercontent.com/62331803/91653289-41724780-eada-11ea-8300-30f8e7cd7b2a.png)
<br/>

![image](https://user-images.githubusercontent.com/62331803/91653292-48995580-eada-11ea-8d0b-e056054be21d.png)
<br/>

# 풀이
#### 문제이해
- N(동전 종류), K(가치의 합)
- A[]: 각 동전의 가치. 오름차순.
-  각 방의 수는 전방의 배수 *왜 필요?
-  K원 만드는 데 필요한 동전 개수의 최소값

#### 의사코드
- k보다 작은 수 중,가장 큰 a값 찾기
- 선택된 a값으로 나눈 몫을 cnt에, 나머지를 k에 삽입
- 해당 시행을 나머지가 없을 때까지 반복

# 코드
#### 1차시도: 반복문 break 설정
- 이유
  - a값 선택하는 코드에서 break문을 주지 않아서
  - 매번 배열 a의 가장 작은 값이 b로 설정됨
- 수정 전
```java
for (i = n - 1; i >= 0; i--) {
				if (a[i] < k) {
					b = a[i];
				}
			}
```
- 수정 후
```java
for (i = n - 1; i >= 0; i--) {
				if (a[i] < k) {
					b = a[i];
					break;//빠져나와야 함. 아니면 제일 작은 값으로 초기화 됨
				}
			}
```
<br/>

#### 2차시도: while문 조건 설정
- 이유
  - while문의 조건을 k>1로 주는 바람에
  - k(나머지)가 1일 경우의 시행을 커버하지 못함
 
 - 수정 전
 ```java while (k > 1)```
 
 - 수정 후 
```java while (k >= 1)```
 
 #### 3차시도: 성공

```java
 import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int i = 0, cnt = 0, n = sc.nextInt(), k = sc.nextInt(), a[] = new int[n];
		for (i = 0; i < n; i++) {
			a[i] = sc.nextInt();
		}

		while (k >= 1) {
			int b = 0;

			for (i = n - 1; i >= 0; i--) {
				if (a[i] <= k) {
					b = a[i];
					break;
				}
			}

			cnt += k / b;
			k %= b;
		}
		System.out.println(cnt);
		sc.close();
	}
}
 ```
 
 # 다른 답안
 
 ```java
import java.io.*;
import java.util.*;
 
public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
   
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(tokenizer.nextToken());
        int k = Integer.parseInt(tokenizer.nextToken());
        int[] coins = new int[n];
        
        for(int i = 0; i < n; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }
        
        int count = 0;
        for(int i = n-1; i >= 0; i--) {
            if(k >= coins[i]) {
                count += k / coins[i];
                k %= coins[i];
            }
        }
        
        bw.write(String.valueOf(count));
 
        br.close();
        bw.close();
    }
}
 ```
 
 #### 속도비교 <br/>
 ![image](https://user-images.githubusercontent.com/62331803/91653428-c7db5900-eadb-11ea-9824-961c3f8e99f1.png)

##### TIP
입출력 BufferedReader와 Scanner의 차이<br/>
https://m.blog.naver.com/PostView.nhn?blogId=occidere&logNo=220811824303&proxyReferer=https:%2F%2Fwww.google.com%2F
 
 
