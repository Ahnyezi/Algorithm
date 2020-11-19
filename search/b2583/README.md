# 백준 2583 | 영역구하기
![image](https://user-images.githubusercontent.com/62331803/96668805-e7ce2100-1396-11eb-8e69-fa86f197de35.png)
<br>

## 문제
 
![image](https://user-images.githubusercontent.com/62331803/96668831-f9172d80-1396-11eb-939d-7e4a5b513554.png)
<br>

## 입력
첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다. 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.


## 출력
첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.


## 입출력 예제
![image](https://user-images.githubusercontent.com/62331803/96668884-13e9a200-1397-11eb-9aa3-506002945cfb.png)
<br>

# 풀이
- 변환1) 이차원 배열에서 알아볼 수 있는 형태로 변환 (y1과 y2에 M 연산)
- 직사각형 부분을 1로 초기화 `(주의할 점) 영역 : y2이상 y1미만, x1이상 x2미만`
```python
import sys
from collections import deque

input = sys.stdin.readline
M,N,K = map(int,input().split()) # M:세로, N:가로, K:사각형 개수
paper = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split()) # 왼쪽 아래 x,y/오른쪽 위 x,y
    y1 = M - y1 # 이차원 리스트에서 처리하기 편한 형태로 변환
    y2 = M - y2 
    for i in range(y2,y1): # y1 > y2
        for j in range(x1,x2): # x1 < x2
            paper[i][j] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False for _ in range(N)] for _ in range(M)]
area = [] # 분리된 각 영역의 넓이
queue = deque()

def bfs(i,j):
    area.append(1)
    queue.append([i,j])
    visited[i][j] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < M and 0 <= new_y < N and paper[new_x][new_y] == 0:
                if not visited[new_x][new_y]:
                    queue.append([new_x,new_y])
                    visited[new_x][new_y] = True
                    area[-1] += 1

for i in range(M):
    for j in range(N):
        if paper[i][j] == 0:
            if not visited[i][j]:
                bfs(i,j)

print(len(area))
print(' '.join(map(str,sorted(area))))
```