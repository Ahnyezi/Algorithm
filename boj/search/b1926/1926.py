# 그림

# 1차시도
# - 외부 배열의 0번째 방부터 순서대로 순회, visited에 삽입
# - 현재방 값이 1이면 상하좌우 검사 : 상 (0,+1) 하 (0,-1) 좌 (-1,0) 우 (+1,0)
# - 1있으면 바로 거기로 가서 visited에 삽입

# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# canvas = [0]*n
# visited = [[0]*n]*m
# direction = [(0,1),(0,-1),(-1,0),(1,0)]
# paints = []
# for i in range(n):
#     canvas[i] = list(map(int,input().split()))
# # print(canvas)
# # print(visited)
# # [[1, 1, 0, 1, 1], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]
# for i in range(n):
#     for j in range(m):
#         if canvas[n][m] == 1:
#

# 2차시도 (답안 보기)
# https://it-garden.tistory.com/173
from collections import deque

n,m = map(int,input().split())

canvas = [list(map(int,input().split())) for i in range(n)] # canvas
ch = [[0]*m for i in range(n)] # visited

# [dx][dy] : 상하좌우 확인용
dx = [-1,0,1,0]
dy = [0,1,0,-1]
paints = [] # paints

print('canvas:',canvas)

def bfs(i,j):
    print('bfs 함수 호출')
    queue = deque()
    queue.append([i,j])
    print('queue:',queue)
    ch[i][j] = 1
    c = 1
    print('ch:',ch)

    while queue:
        x,y = queue.popleft()
        print('queue의 0번방 pop>>',end='')
        print(x,y)

        print('상하좌우 검사')
        for i in range(4): # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m: # 범위 안에서만 check
                if ch[nx][ny] == 0 and canvas[nx][ny] != 0: # 아직 방문 X and 배열방 1
                    print('nx:',str(nx),'/ny:',str(ny))
                    print('조건만족')
                    canvas[nx][ny] = canvas[x][y] + 1 # ?
                    ch[nx][ny] = 1 # visited에 체크

                    c += 1
                    queue.append([nx,ny]) # ?
                    print('canvas:',canvas)
                    print('ch:',ch)
                    print('queue:',queue)
                    print('c:',c)
        print()

    paints.append(c) # 그림크기 (이어져있는 1개수)
    print('paints:',paints)

for i in range(n):
    for j in range(m):
        if canvas[i][j] == 1:
            bfs(i,j)
if len(paints) == 0:
   print(len(paints))
   print(0)
else:
    print(len(paints))
    print(max(paints))
