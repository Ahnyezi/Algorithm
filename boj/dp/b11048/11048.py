# 이동하기
# 0,0에서 N,M으로 이동할 때 가져올 수 있는 사탕개수 최댓값 (브루트포스, DP, DFS)
# dfs 써서 모든 경우 구하는 거 같은데 어케 해야될지 모르겠군


# 1차 모르게떠 ㅠㅠ
# import sys
#
# input = sys.stdin.readline
# n,m = map(int,input().split())
# maze = [[0 for _ in range(m)] for _ in range(n)]
# visited = [[False for _ in range(m)] for _ in range(n)] # 매번 새롭게
# for i in range(n):
#     maze[i] = list(map(int,input().split()))
#
# dx = [1,0,1]
# dy = [0,1,1]
#
# def dfs(x,y):
#     if x == n-1 and y == m-1:
#         return maze[n-1][m-1]
#     for i in range(3):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m: # 전체 경우 다 구해야 되는데
#             return dfs(nx,ny)
#
# print(dfs(0,0))

## 참고
# 핵심은 점화식 세우기
# lcs와 비슷한 논리다
import sys, time
input = sys.stdin.readline
n,m = map(int,input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input().split())))
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = maze[i][j] + max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
print(dp[n][m])