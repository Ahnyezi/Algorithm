# 백준 2667 | 단지번호 붙이기
![image](https://user-images.githubusercontent.com/62331803/98539472-bb3f6200-22cf-11eb-99ff-895d0a2969fc.png)
<br>

## 문제
![image](https://user-images.githubusercontent.com/62331803/98539509-ceeac880-22cf-11eb-8e7c-be385e66ac3e.png)

## 입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.


## 출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

## 입출력 예제
![image](https://user-images.githubusercontent.com/62331803/98539592-f477d200-22cf-11eb-969f-d431f97cb980.png)
<br>


# 풀이
## 1차 시도(예제 O, 채점 X)

```python
from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
m = [[0 for _ in range(N)] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
queue = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]
house_complex = 1 # 단지 번호
houses = [] # 단지별 집 수

for i in range(N):
     m[i] = list(map(int,list(input().rstrip())))

def bfs(comp):
    houses.append(1)
    while queue:
        x,y = queue.popleft()
        m[x][y] = house_complex
        visited[x][y] = 1
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N and m[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                m[new_x][new_y] = house_complex
                houses[-1] += 1
                queue.append([new_x,new_y])

for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            queue.append([i,j])
            house_complex += 1
            bfs(house_complex)

sorted(houses) # 오류부분 => houses = sorted(houses) 로 변경해야 함
print(len(houses))
for h in houses:
    print(h)
```

## 2차시도 (반례에서 문제 찾음. 정렬 제대로 안되었음)
- sorted()함수로 정렬할 경우, 다시 변수에 넣어줘야 함.
    - houses = sorted(houses) 
- houses.sort() 사용 가능

```python
from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
m = [[0 for _ in range(N)] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
queue = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]
house_complex = 1 # 단지 번호
houses = [] # 단지별 집 수

for i in range(N):
     m[i] = list(map(int,list(input().rstrip())))

def bfs(house_complex):
    houses.append(1)
    while queue:
        x,y = queue.popleft()
        m[x][y] = house_complex
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N and m[new_x][new_y] == 1:
                m[new_x][new_y] = house_complex
                houses[-1] += 1
                queue.append([new_x,new_y])

for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            queue.append([i,j])
            house_complex += 1
            bfs(house_complex)

houses.sort()
print(len(houses))
for h in houses:
    print(h)
```


# 피드백
- 정렬함수 사용방법 주의
    - sorted()는 변수에 다시 삽입
    - arr.sort()는 삽입할 필요 없음