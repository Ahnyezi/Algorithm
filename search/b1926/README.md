# 백준 1926 | 그림

![image](https://user-images.githubusercontent.com/62331803/96589742-2674c480-1320-11eb-8f49-6eb8395ea705.png)
<br>

## 문제
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.


## 입력
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

## 출력
첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

## 입출력 예제

![image](https://user-images.githubusercontent.com/62331803/96589827-40aea280-1320-11eb-8b49-e9619af653f5.png)
<br>

# 풀이
## 1차 (모르겠써)
- 외부 배열의 0번째 방부터 순서대로 순회, visited에 삽입
- 현재방 값이 1이면 상하좌우 검사 : 상 (0,+1) 하 (0,-1) 좌 (-1,0) 우 (+1,0)
- 1있으면 바로 거기로 가서 visited에 삽입

```python
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
canvas = [0]*n
visited = [[0]*n]*m
direction = [(0,1),(0,-1),(-1,0),(1,0)]
paints = []
for i in range(n):
    canvas[i] = list(map(int,input().split()))
# print(canvas)
# print(visited)
# [[1, 1, 0, 1, 1], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]
for i in range(n):
    for j in range(m):
        if canvas[n][m] == 1:
```

## 2차 (답안 참고) => 성공

- 참고: https://it-garden.tistory.com/173

> 전체 구조
- 너비우선탐색 (queue 활용)
   - 모든 배열방을 순회하면서 => `for i in range (n): for j in range(m):`
   - 조건에 맞는 배열방에 들어가 =>` if i == 1: # (0:그림 아님/1 이상:처리 완료)`
   - 너비를 우선으로 탐색 => `for i in range(4): nx = x(현재) + dx(주변); ny = y(현재) + dy(주변)`
- 배열 dx와 dy는 너비우선탐색을 위한 인덱스 값들
- 모든 방을 순회하면 종료 후 "paints 배열 길이와 최대값" 출력

> bfs 함수 내부 알고리즘
1. bfs(i,j) 호출
<br>

2. 큐 생성 (이차원 배열의 x,y좌표)
- `queue = deque ([i,j])`
3. visted 배열에 (i,j)방 check
- `visted[i][j] = 1`
4. 그림 개수 초기화
- `cnt = 1`
<br>

5. queue의 길이가 0이 될 때까지 반복
- `while queue:`
6. queue의 0번째방 pop
- `x,y = queue.popleft()`
7. 상하좌우 검사
- `for i in range(4): nx = x + dx[i]; ny = y + dy[i]`
<br>

8. 그림개수연산 조건 확인
- 이차원 배열 범위 한정
    - `if 0 <= nx < n and  0 <= ny < m:`
- 아직 방문하지 않았으면서 값이 1인 배열방에 진입
    - `if visited[nx][ny] == 0 and canvas[nx][ny] != 0 :`
9. 현재 배열방의 상하좌우방이 2가지 조건에 맞는 경우 
- 상하좌우방에 현재방 + 1 연산을 해주고, 방문했음을 체크
    - `canvas[nx][ny] = canvas[x][y] + 1`
    - `visited[nx][ny] = 1`
- 그림 개수 증가시키기
    - `cnt += 1`
- 조건에 맞은 상하좌우방 인덱스 queue에 삽입 (해당 방은 그림이 있기 때문에, 그 방 상하좌우 다시 검사 필요)
    - `queue.append([nx,ny])`
<br>

10. queue 길이가 0이 되면 반복종료
- queue에서 연산한 cnt(연결된 그림의 size)를 paints(그림들) 배열에 삽입
    - `paints.append(cnt)`
<br>


```python
from collections import deque

n,m = map(int,input().split())

canvas = [list(map(int,input().split())) for i in range(n)]
visited = [[0]*m for i in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
paints = []

def bfs(i,j):
    queue = deque()
    queue.append([i,j])
    visited[i][j] = 1
    cnt = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4): # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m: # 범위 안에서만 check
                if visited[nx][ny] == 0 and canvas[nx][ny] != 0: # 아직 방문 X and 배열방 1
                    canvas[nx][ny] = canvas[x][y] + 1 # 현재까지 합한 그림 size (이미 연산완료했다는 check)
                    visited[nx][ny] = 1 # visited에 체크

                    cnt += 1
                    queue.append([nx,ny]) # 1이 있는 그 위치 queue방에 삽입

    paints.append(cnt) # 그림크기 (이어져있는 1개수)

for i in range(n): # 모든 배열을 검사
    for j in range(m): # 1이지만 아직 처리도 안된 방을 검사 (처리 후:1 이상)
        if canvas[i][j] == 1:
            bfs(i,j)
if len(paints) == 0:
   print(len(paints))
   print(0)
else:
    print(len(paints))
    print(max(paints))

```

# 피드백


> 참고: deque 사용 이유
- 정의
   - deque: 스택과 큐를 합친 자료구조
   - 가장자리에 원소를 넣거나 뺄 수 있음
- 함수
   - deque() : 초기화
   - append(x) : x를 덱의 오른쪽에 삽입
   - popleft() : 덱의 가장 왼쪽에 있는 원소를 제거, 해당 값을 리턴
   - clear() : 모든 원소 삭제
- 특징
   - 큐 구현에 list를 사용하지 않음
       - list도 사용가능. 하지만
       - pop()의 시간복잡도는 O(1)
       - pop(0)의 시간복잡도는 O(N)
       - 따라서 시간복잡도를 고려해 list를 큐로 사용하지 않음

