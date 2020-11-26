# 욕심쟁이 판다

## ^^ 모르게써
# import sys
#
# input = sys.stdin.readline
# n = int(input())
# forest = []
# for _ in range(n):
#     forest.append(list(map(int,input().split())))
# dp = [[1 for _ in range(n)] for _ in range(n)]
#
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
#
# def dfs(i,j):
#     stack = [[i,j]]
#     cnt = [0,0,0,0]
#     while stack:
#         x,y = stack.pop()
#         for k in range(4):
#             flag = False
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if forest[nx][ny] > forest[x][y]:
#                     stack.append([nx,ny])
#                     flag = True
#             if flag:
#                 cnt[k] += 1
#     print(cnt)
#     if i == 1:
#         print(input())
#
# for i in range(n):
#     for j in range(n):
#         dfs(i,j)
#
# for i in range(len(dp)):
#     print(dp[i])
#
# print(max(dp))

# 참고
# from sys import setrecursionlimit
# setrecursionlimit(10**9)
#
# def dfs(x,y):
#     if visited[x][y] < 0: # 이미 최대경로가 구해져 있는 경우에는 파생 연산없이 바로 return 한다
#         visited[x][y] = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and forest[x][y] < forest[nx][ny]:
#                 visited[x][y] = max(visited[x][y],dfs(nx,ny)) # 현재칸으로 부터 파생된 칸에서 max count 값으로 visited를 초기화
#         visited[x][y] += 1 # 현재 칸을 방문했다는 count +1 추가
#     return visited[x][y]
#
# n = int(input())
# forest = [list(map(int,input().split())) for _ in range(n)]
# visited = [[-1] * n for _ in range(n)] # 방문여부와 cnt 함께 고려할 수 있게 -1로 초기화
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# ans = 0
# for i in range(n):
#     for j in range(n): # 매 시행마다 비교하여 최댓값을 초기화
#         ans = max(ans,dfs(i,j))
#
# for i in range(len(visited)):
#     print(visited[i])

# 다시 풀어보기
# - dfs와 dp를 사용
#    - dfs로 구할 수 있는 모든 경우를 비교하여 최댓값을 return 한다.

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and forest[x][y] < forest[nx][ny]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny))
        dp[x][y] += 1
    return dp[x][y]

max_days = 0
for i in range(n):
    for j in range(n):
        max_days = max(max_days, dfs(i, j))
print(dp, end='\n\n')
print(max_days)
