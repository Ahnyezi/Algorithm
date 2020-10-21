# 영역 구하기
# - 너비우선탐색 (queue 사용)

import sys
from collections import deque

input = sys.stdin.readline
m,n,k = map(int,input().split()) # m:세로/n:가로/k:직사각형개수
canvas = [[0]*n for _ in range(m)]
print(canvas)
for _ in range(k):
    x1, y1, x2, y2 = map(int,input().split())
    print(x1, y1, x2, y2)
    canvas[x1][y1] = 1
    canvas[x2][y2] = 1
visited = [[0]*n for _ in range(m)]
regions = []
dx = [-1,0,1,0]
dy = [0,-1,0,1]

print(canvas)

def bfs(i,j):
    queue = deque([[i,j]])
    visited[i][j] = 1


    pass

if __name__ == '__main__':
    for i in range(n):
        for j in range(m):
            if canvas[i][j] == 1:
                bfs(i,j)
    print(*regions)



