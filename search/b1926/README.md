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

## 2차 (답안 참고)

- https://it-garden.tistory.com/173
- 너비우선탐색 사용

```python
from collections import deque

n,m = map(int,input().split())

canvas = [list(map(int,input().split())) for i in range(n)] # canvas
ch = [[0]*m for i in range(n)] # visited

# [dx][dy] : 상하좌우 확인용
dx = [-1,0,1,0]
dy = [0,1,0,-1]
paints = [] # paints

print('canvas:',canvas)

def bfs(i,j):
    print('bfs 함수 호출')
    queue = deque()
    queue.append([i,j])
    print('queue:',queue)
    ch[i][j] = 1
    c = 1
    print('ch:',ch)

    while queue:
        x,y = queue.popleft()
        print('queue의 0번방 pop>>',end='')
        print(x,y)

        print('상하좌우 검사')
        for i in range(4): # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m: # 범위 안에서만 check
                if ch[nx][ny] == 0 and canvas[nx][ny] != 0: # 아직 방문 X and 배열방 1
                    print('nx:',str(nx),'/ny:',str(ny))
                    print('조건만족')
                    canvas[nx][ny] = canvas[x][y] + 1 # ?
                    ch[nx][ny] = 1 # visited에 체크

                    c += 1
                    queue.append([nx,ny]) # ?
                    print('canvas:',canvas)
                    print('ch:',ch)
                    print('queue:',queue)
                    print('c:',c)
        print()

    paints.append(c) # 그림크기 (이어져있는 1개수)
    print('paints:',paints)

for i in range(n):
    for j in range(m):
        if canvas[i][j] == 1:
            bfs(i,j)
if len(paints) == 0:
   print(len(paints))
   print(0)
else:
    print(len(paints))
    print(max(paints))
```
