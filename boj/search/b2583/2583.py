# 영역 구하기
# : 직사각형으로 나눠진 각 구역들의 넓이를 담은 리스트 출력

# 0 2 4 4 -> 0 3 4 1 /=> 높이 1 3 너비 0 4
# 1 1 2 5 -> 1 4 2 0 /=> 높이 0 4 너비 1 2
# 4 0 6 2 -> 4 5 6 3 /=> 높이 3 5 너비 4 6

# 1차 (맞아따 뀨ㅠㅠ,,)
import sys
from collections import deque

input = sys.stdin.readline
M,N,K = map(int,input().split()) # M:세로, N:가로, K:사각형 개수
paper = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split()) # 왼쪽 아래 x,y/오른쪽 위 x,y
    y1 = M - y1
    y2 = M - y2
    for i in range(y2,y1):
        for j in range(x1,x2):
            paper[i][j] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False for _ in range(N)] for _ in range(M)]
area = []
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




