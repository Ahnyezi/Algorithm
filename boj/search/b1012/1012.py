# 유기농 배추
# 이어져 있는 1이 있는 구간에 한 개씩
# bfs로 주변에 있는 1 처리

## 1차 (시간 초과)
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
