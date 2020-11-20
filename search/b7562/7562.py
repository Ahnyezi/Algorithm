# 나이트의 이동
# 최단거리(bfs)

import sys
from collections import deque

input = sys.stdin.readline

dx = [2,1,2,1,-2,-1,-2,-1]
dy = [-1,-2,1,2,-1,-2,1,2]

count = []
T = int(input())
for _ in range(T):
    I = int(input())
    board = [[0 for _ in range(I)] for _ in range(I)]
    visited = [[False for _ in range(I)] for _ in range(I)] # 안해주면 짱 느려
    x, y = map(int,input().split()) # 순서 ? (상관 없나?)
    goal_x, goal_y = map(int,input().split()) # 순서 ?

    if x == goal_x and y == goal_y:
        print(0)
    else:
        queue = deque([[x, y]])
        visited[x][y] = True
        while queue:
            x, y = queue.popleft()
            for i in range(8):
                new_x = x + dx[i] #
                new_y = y + dy[i] #
                if 0 <= new_x < I and 0 <= new_y < I:
                    if not visited[new_x][new_y]:
                        board[new_x][new_y] = board[x][y] + 1
                        queue.append([new_x,new_y])
                        visited[new_x][new_y] = True
            if not board[goal_x][goal_y] == 0:
                break
        print(board[goal_x][goal_y])
