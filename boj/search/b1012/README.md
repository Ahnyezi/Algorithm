# 백준 1012 | 유기농 배추

![image](https://user-images.githubusercontent.com/62331803/98461737-071bd980-21f2-11eb-916a-cf51029db8a3.png)

## 문제

![image](https://user-images.githubusercontent.com/62331803/98461752-26b30200-21f2-11eb-9272-95cf862c9c48.png)
<br>

## 입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.

## 출력
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

## 입출력 예제
![image](https://user-images.githubusercontent.com/62331803/98461765-40ece000-21f2-11eb-8d8e-e04cbc918f05.png)
<br>

![image](https://user-images.githubusercontent.com/62331803/98461769-4d713880-21f2-11eb-8347-9f06fec66fbd.png)
<br>

# 풀이

## 1차시도 (예제 O, 채점 시간초과) 왜...?

```python
from _collections import deque

def bfs(i, j):
    queue = deque([[i,j]])
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < M and visited[new_x][new_y] == 0 and field[new_x][new_y] == 1:
                queue.append([new_x, new_y])

dx = [-1,0,1,0]
dy = [0,-1,0,1]

t = int(input())
for _ in range(t):
    M,N,K = map(int,input().split())

    field = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    for _ in range(K):
        y,x = map(int,input().split())
        field[x][y] = 1

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                bfs(i,j)
    print(cnt)

```