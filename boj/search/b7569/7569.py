# 토마토

## 1차시도 (while문에서 break 안됨)

# from _collections import deque
# 
# dx = [-1,1,0,0,0,0]
# dy = [0,0,-1,1,0,0]
# dz = [0,0,0,0,-1,1]
# 
# def bfs(i,j,k):
#     print('bfs 함수 호출')
#     global cnt
#     queue = deque([[i,j,k]])
#     visited[i][j][k] = 1
#     while queue:
#         x,y,z = queue.popleft()
#         for i in range(6):
#             new_x = x + dx[i]
#             new_y = y + dy[i]
#             new_z = z + dz[i]
#             if 0 <= new_x < H and 0 <= new_y < N and 0 <= new_z <M and visited[new_x][new_y][new_z] == 0:
#                 if box[new_x][new_y][new_z] == 0:
#                     box[new_x][new_y][new_z] += 1
#                     # queue.append([new_x,new_y,new_z])
#                 elif box[new_x][new_y][new_z] == 1:
#                     queue.append([new_x,new_y,new_z])
#         cnt += 1
#         print('queue:',queue)
#         print('box:',box)
#         print('visited:',visited)
#         print()
# 
# M,N,H = map(int,input().split())
# box = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
# visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
# cnt = 0
# 
# for i in range(H): # 높이
#     for j in range(N): # 세로
#         box[i][j] = list(map(int,input().split()))
# 
# for i in range(H):
#     for j in range(N):
#         for k in range(M):
#             if box[i][j][k] == 1 and visited[i][j][k] == 0: # 익은 토마토
#                 bfs(i,j,k)

# ## 2차 시도 (알고리즘 참고) https://pacific-ocean.tistory.com/297
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
