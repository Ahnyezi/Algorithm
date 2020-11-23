
# ## 1차 (모르겠오)
# N,M = map(int,input().split())
# maze = [0]*N
# for i in range(N):
#     maze[i] = list(map(int,list(input())))
# # print(maze)
# visited = [[0]*M]*N
# dx = [-1,0,1,0]
# dy = [0,-1,0,1]
# cnt = 0
#
# for i in range(M):
#     for j in range(N):
#         if visited[i][j] == 0:
#             if 0 <= i < M and 0 <= j < N:
#                 visited[i][j] = 1

# ## 2차(알고리즘 참고)
# 최단거리를 dfs로 풀면 시간복잡도가 엄청나진다.
# 경로가 아주 많을 수 있기 때문
# 따라서 최단거리 문제는 bfs로 풀어야 한다.
# n,m = map(int,input().split())
# s = []
# queue = []
# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
# for i in range(n):
#     s.append(list(map(int,input())))
# print(s)
# queue = [[0,0]]
# # s[0][0] = 1 #?
# # print(s)
# while queue:
#     a,b = queue[0][0],queue[0][1] # ok
#     del queue[0]
#     for i in range(4):
#         x = a + dx[i]
#         y = b + dy[i]
#         if 0 <= x < n and 0 <= y < m and s[x][y] == 1:
#             queue.append([x,y])
#             s[x][y] = s[a][b]+1
# print(s,end='\n')
# print(s[n-1][m-1])

N,M = map(int,input().split())
maze = [0]*N
for i in range(N):
    maze[i] = list(map(int,list(input())))
dx = [1,-1,0,0]
dy = [0,0,-1,1]
queue = [[0,0]]
print(maze)
while queue:
    x,y = queue[0][0],queue[0][1]
    del queue[0]
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        ## N과 M의 위치?
        if 0 <= new_x < N and 0 <= new_y < M and maze[new_x][new_y] == 1:
            queue.append([new_x,new_y])
            maze[new_x][new_y] = maze[x][y]+1
print(maze)
print(maze[N-1][M-1])