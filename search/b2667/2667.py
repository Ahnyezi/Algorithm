# 단지번호 붙이기

# ## 1차 (예제 o, 채점 x)
# from collections import deque
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# m = [[0 for _ in range(N)] for _ in range(N)]
# visited = [[0 for _ in range(N)] for _ in range(N)]
# queue = deque()
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# house_complex = 1 # 단지 번호
# houses = [] # 단지별 집 수
#
# for i in range(N):
#      m[i] = list(map(int,list(input().rstrip())))
#
# def bfs(comp):
#     houses.append(1)
#     while queue:
#         x,y = queue.popleft()
#         m[x][y] = house_complex
#         visited[x][y] = 1
#         for i in range(4):
#             new_x = x + dx[i]
#             new_y = y + dy[i]
#             if 0 <= new_x < N and 0 <= new_y < N and m[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
#                 m[new_x][new_y] = house_complex
#                 houses[-1] += 1
#                 queue.append([new_x,new_y])
#
# for i in range(N):
#     for j in range(N):
#         if m[i][j] == 1:
#             queue.append([i,j])
#             house_complex += 1
#             bfs(house_complex)
#
# sorted(houses) # 오류부분 => houses = sorted(houses) 로 변경해야 함
# print(len(houses))
# for h in houses:
#     print(h)

## 2차
from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
m = [[0 for _ in range(N)] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
queue = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]
house_complex = 1 # 단지 번호
houses = [] # 단지별 집 수

for i in range(N):
     m[i] = list(map(int,list(input().rstrip())))

def bfs(house_complex):
    houses.append(1)
    while queue:
        x,y = queue.popleft()
        m[x][y] = house_complex
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N and m[new_x][new_y] == 1:
                m[new_x][new_y] = house_complex
                houses[-1] += 1
                queue.append([new_x,new_y])

for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            queue.append([i,j])
            house_complex += 1
            bfs(house_complex)

houses.sort()
print(len(houses))
for h in houses:
    print(h)
