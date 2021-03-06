# 문제2839 | 설탕배달 (못풂)
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. <br/>
상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.  <br/>
설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다. <br/>
<br/>
상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.  <br/>
예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만,  <br/>
5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다. <br/>
<br/>
상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오. <br/>
<br/>

#### 입력
첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000) <br/>

#### 출력
상근이가 배달하는 봉지의 최소 개수를 출력한다.  <br/>
만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
<br/>

#### 입출력 예제
<img src="https://user-images.githubusercontent.com/62331803/91651455-de77b500-eac7-11ea-9da0-911e9d635a61.png" width="60%">

# 풀이

#### 문제이해
- nkg의 설탕을 배달
- nkg = 5kg x a개 + 3kg x b + c
- 봉지 수가 최소가 되기위해서 a의 값이 최대가 되는 경우를 구해야 함
<br/>

#### 의사코드
- n을 입력받아, n자체에 연산을 지속하며 값을 줄여나감.
- n이 5로 나누어 떨어지지 않을 경우, ```java n-=3; cnt++;```
- n이 5로 나누어 떨어지는 경우, ```java return cnt + n/5```;
- n이 0보다 작아진 경우, ```java return -1```.

<br/>

#### 피드백
` 백준은 Scanner로 입력받아서 System으로 출력하는 것으로 채점`
- n%5==0인 상황을 만들기 위해서 -3을 우선적으로 처리해준다.<br/>
```java
while (n % 5 != 0 && n > 0) {
			n -= 3;
			cnt++;
		}
```
- 5와 3으로 처리 불가능한 영역은 n이 음수가 되는 경우로 한번에 처리

# 다른답안
```java
import java.util.Scanner;

public class Main {
    public static int nThree;
    public static int answer;
	
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
    	
        while(n % 5 != 0 && n >= 0) {
            n -= 3;
            ++nThree;
        }
        answer = n < 0 ? -1 : nThree + n/5; //조건 삼항 처리
        
        System.out.println(answer);
    }
}
```
