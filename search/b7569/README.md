# 백준 7569 | 토마토
## 문제
![image](https://user-images.githubusercontent.com/62331803/98467857-064b6d80-221b-11eb-862a-67c005155546.png)

## 입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다. 둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다. 각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 이러한 N개의 줄이 H번 반복하여 주어진다.

## 출력
여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.


## 입출력 예제
![image](https://user-images.githubusercontent.com/62331803/98467875-21b67880-221b-11eb-8d3c-d29f72b9824d.png)
<br>

![image](https://user-images.githubusercontent.com/62331803/98467885-2e3ad100-221b-11eb-95f5-e818dea77c3c.png)
<br>

![image](https://user-images.githubusercontent.com/62331803/98467888-3561df00-221b-11eb-98f0-8cdb8a80ee46.png)
<br>

# 풀이
## 1차시도 (while문에서 break 안됨)
```python
from _collections import deque

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs(i,j,k):
    print('bfs 함수 호출')
    global cnt
    queue = deque([[i,j,k]])
    visited[i][j][k] = 1
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            new_x = x + dx[i]
            new_y = y + dy[i]
            new_z = z + dz[i]
            if 0 <= new_x < H and 0 <= new_y < N and 0 <= new_z <M and visited[new_x][new_y][new_z] == 0:
                if box[new_x][new_y][new_z] == 0:
                    box[new_x][new_y][new_z] += 1
                    # queue.append([new_x,new_y,new_z])
                elif box[new_x][new_y][new_z] == 1:
                    queue.append([new_x,new_y,new_z])
        cnt += 1
        print('queue:',queue)
        print('box:',box)
        print('visited:',visited)
        print()

M,N,H = map(int,input().split())
box = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
cnt = 0

for i in range(H): # 높이
    for j in range(N): # 세로
        box[i][j] = list(map(int,input().split()))

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1 and visited[i][j][k] == 0: # 익은 토마토
                bfs(i,j,k)

```

## 2차시도 (알고리즘 참고 -> 성공)
- 익은 토마토의 위치를 미리 queue에 모두 삽입하고 bfs함수 호출
- bfs 함수 호출 이후, 내부에서 익은 토마토 주변의 토마토의 값을 +1 
- bfs 함수 종료 이후, 0인 토마토 존재유무에 따라 구분
   - 0인 토마토 존재(flag == True) : -1
   - 0인 토마토 존재안함(flag == False) : max_day - 1  
```python
from collections import deque
import sys
input = sys.stdin.readline
dx = [1,-1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
    while queue:
        x, y, z = queue.popleft()  # H N M
        visited[x][y][z] = 1
        for i in range(6):
            new_x = x + dx[i]
            new_y = y + dy[i]
            new_z = z + dz[i]
            if 0 <= new_x < H and 0 <= new_y < N and 0 <= new_z < M and box[new_x][new_y][new_z] == 0 and visited[new_x][new_y][new_z] == 0:
                queue.append([new_x,new_y,new_z])
                box[new_x][new_y][new_z] = box[x][y][z] + 1
                visited[new_x][new_y][new_z] = 1

M,N,H = map(int,input().split())
box = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
queue = deque()
for i in range(H):
    for j in range(N):
        box[i][j] = list(map(int,input().split()))

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                queue.append([i,j,k])

bfs()

flag = False # 익지 않은 토마토 존재유무
max_day = 0 # 최소 일수
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                flag = True
                break
            else:
                max_day = max(max_day,box[i][j][k])

if flag:
    print(-1)
else:
    print(max_day - 1)

```
<br>

# 피드백
- 3차원 배열의 경우 dx,dy,dz 각각 6개씩
- 익은 토마토 발견할 때마다 bfs를 호출하는 것이 아니라, 익은 토마토 인덱스 모두 삽입 후에 한꺼번에 bfs() 호출해서 처리
- bfs() 호출 이후에도 익지 않은 토마토 구별해내기 위한 불린타입 변수 마련하기
