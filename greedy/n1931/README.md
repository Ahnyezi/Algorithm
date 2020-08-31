(8/31 월)

# 문제 1931 | 회의실 배정 (오답+개오래걸림) ☆☆☆☆

## 피드백

### 1. 입출력 예제에 힌트가 있다! <br/>
<details>
	<summary>열기</summary>
  <img src="https://user-images.githubusercontent.com/62331803/91730194-9b5d3500-ebe0-11ea-8c55-b3282fd557f6.png" width="20%"> <br/>
	
  - 입력 예제: 이미 정렬되어 있는 상태
  - 정렬된 방식을 봐라 ==> 종료시간을 기준으로 정렬
</details>

### 2. 정렬 방법 다양하게 생각 못함<br/>
<details>
	<summary>열기</summary>
	
  - 방법1: 시작시간 기준 정렬 (반례 O) <br/>
  <img src="https://user-images.githubusercontent.com/62331803/91729840-1a05a280-ebe0-11ea-8ed5-c58760190b1c.png" width="50%">
  <br/>
  
  - 방법2(내가 푼 방식): 회의시간 기준 정렬 (반례 O) <br/>
  <img src="https://user-images.githubusercontent.com/62331803/91729866-225ddd80-ebe0-11ea-8d5b-f7689e160104.png" width="50%">
  <br/>
  
  - 방법3: 종료시간 기준 정렬 (일부 예외만 처리한다면 적합 => 시작,종료시간 같은 경우)
    - `예시` 
    ```python
    def greedy(meeting):
    end_time = 0 # 이전 회의의 종료시간
    meeting_count = 0

    for time in meeting:
        if end_time <= time[0]: # 이전 회의 종료시간 <= 현재 회의 시작시간
            meeting_count += 1
            end_time = time[1] # 현재 회의 종료시간
    return meeting_count
    ```
    - (2,2) (1,2) ...의 경우
    - 종료시간만을 기준으로 sorting 하면 모든 경우를 cover하지 못함
    - end_time이 2일 때 time[0]인 1이 더 작기 때문에, meeting_count에 포함될 수 없음
    - 따라서, 종료시간으로 sorting 하기 전에 시작시간으로 미리 sorting 해서
    - 이런 case를 cover한다

</details>

### 3. 파이썬이 훨씬 간단<br/>

  - 지금 내 수준에서 파이썬으로 알고리즘 공부한 뒤에 자바로 바꾸는 게 낫겠다

<br/>

## 문제
<details>
<summary> 문제보기 </summary>

한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.<br/>
<br/>
#### 입력
첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.<br/>
<br/>
#### 출력
첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.<br/>
</details>

<br/>

## 풀이

#### 문제이해
- 한 개의 회의실을 n개의 회의가 사용하려함
- 회의가 겹치지 않게 사용할 수 있는 회의 최대 개수
- 단! **회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있으며**,
- **회의의 시작시간과 끝나는 시간이 같을 수 있다**

#### 의사코드(오답)
- 회의 진행시간을 기준으로 오름차순 정렬한 뒤
- 리스트의 첫번째 방부터 꺼내어 회의 개수를 카운트

<br/>


## 전체코드

#### python

```python
# 1. 리스트 정렬
#   <정렬방법>
#   1) 시작 시간을 기준으로 (x)
#   2) 회의 지속 시간을 기준으로 (x)
#   3) 종료 시간을 기준으로 (o)
# 2. 정렬된 리스트에서 하나씩 뽑아서 회의 배치

import sys

def greedy(meeting):
    end_time = 0 # 이전 회의의 종료시간
    meeting_count = 0

    for time in meeting:
        if end_time <= time[0]: # 이전 회의 종료시간 <= 현재 회의 시작시간
            meeting_count += 1
            end_time = time[1] # 현재 회의 종료시간
    return meeting_count

if __name__ == "__main__" :
    meeting = []
    mCount = int(sys.stdin.readline())
    for i in range(mCount):
        start, end = map(int, sys.stdin.readline().split())
        meeting.append((start,end))
    print(meeting)

    meeting = sorted(meeting, key=lambda time:time[0])
    print("시작시간으로 정렬:",meeting)
    meeting = sorted(meeting, key=lambda time:time[1])
    print("종료시간으로 정렬:",meeting)

    print('meeting_count:',greedy(meeting))

'''
<결과>
[(1, 4), (3, 5), (3, 4), (2, 2), (1, 2)]
시작시간으로 정렬: [(1, 4), (1, 2), (2, 2), (3, 5), (3, 4)]
종료시간으로 정렬: [(1, 2), (2, 2), (1, 4), (3, 4), (3, 5)]
3
'''
```

#### java

<details>
<summary>코드보기</summary>

```java
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

```

</details>
