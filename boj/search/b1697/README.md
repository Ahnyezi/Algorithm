# 백준 1697 | 숨바꼭질

![image](https://user-images.githubusercontent.com/62331803/98513654-8b7e6300-22ab-11eb-9281-0d41617c4859.png)
<br>

## 문제 
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

## 입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.


## 출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.


## 입출력 예제

![image](https://user-images.githubusercontent.com/62331803/98513736-b2d53000-22ab-11eb-96de-c92d3a75c374.png)
<br>

# 풀이
## 1차 (알고리즘 참고 -> 성공)
- queue배열에 연산 결과와 횟수를 함께 저장
- queue가 아닌 다른 배열 만들어서 연산 결과 따로 저장할 필요 없음.

```python
from collections import deque
N,K = map(int,input().split()) # N:기준점, K:목표지점
visited = [0 for i in range(100001)] # 최대값크기의 배열
queue = deque()
queue.append([N,0]) # 기준점, 횟수

while queue:
    point, cnt = queue.popleft()
    if point == K:
        print(cnt)
        break
    visited[point] = 1
    if point-1 >= 0 and visited[point-1] == 0:
        queue.append([point-1,cnt+1])
    if point+1 <= 100000 and visited[point+1] == 0:
        queue.append([point+1,cnt+1])
    if point*2 <= 100000 and visited[point*2] == 0:
        queue.append([point*2,cnt+1])

```

# 피드백
-  연산결과와 횟수를 함께 저장하는 방식사용하기
    -  `queue.append([point-1,cnt+1])`
