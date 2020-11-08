# 토마토
from _collections import deque

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs(i,j,k):
    queue = deque([i,j,k])
    visited[i][j][k] = 1
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            new_x = x + dx[i]
            new_y = y + dy[i]
            new_z = z + dz[i]
            if 0 <= new_x < H and 0 <= new_y < N and 0 <= new_z <M \
                and visited[new_x][new_y][new_z] == 0 and box[new_x][new_y][new_z] != -1:
                queue.append([new_x,new_y,new_z])

M,N,H = map(int,input().split())
box = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

for i in range(H): # 높이
    for j in range(N): # 세로
        box[i][j] = list(map(int,input().split()))

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1 and visited[i][j] == 0:
                bfs(i,j,k)


