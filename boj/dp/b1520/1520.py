# 내리막 길

## 1차 (시간 초과)

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# M,N = map(int,input().split()) # 세로 M,가로 N <= 500
# m = [0 for _ in range(M)]
# for i in range(M):
#     m[i] = list(map(int,input().split()))
#
# dp = [[0 for _ in range(N)]for _ in range(M)]
#
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
#
# queue = deque([[0,0]])
# while queue:
#     x,y = queue.popleft()
#     height = m[x][y]
#     for i in range(4):
#         new_x = x + dx[i]
#         new_y = y + dy[i]
#         if 0 <= new_x < M and 0 <= new_y < N and m[new_x][new_y] < height:
#             print(new_x,new_y)
#             dp[new_x][new_y] += 1 # 해당 idx 지나갈 때마다 1씩 더하기
#             print(dp[new_x][new_y])
#             print()
#             queue.append([new_x,new_y])
#
# # for i in range(M):
# #     print(dp[i])
#
# print(dp[M-1][N-1])

## 설명참고 (https://chldkato.tistory.com/114)
# import sys
#
# input = sys.stdin.readline
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# def dfs(x,y): # 왜 dfs로 하는건가? 재귀랑 dfs 내용 다시 보기
#     if x == m-1 and y == n-1: # 종료 조건1: 목표 지점에 도달했다면, 1을 반환
#         return 1 # 끝의 경우부터 되돌아가며 연산한다고 생각해라
#     if c[x][y] != -1: # 종료 조건2: 이미 방문한 경우, dp 배열의 원소를 반환
#         return c[x][y]
#
#     c[x][y] = 0 # 아래의 if 문에서 걸리지 않는 경우엔 0으로 남는다
#                 # 방문했지만 크거나 같은 값이라 조건에 안맞는 경우
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < m and 0 <= ny < n:
#             if a[nx][ny] < a[x][y]: # 새로운 idx의 원소가 기존 원소보다 작은 경우
#                 # 즉, 새 idx 원소가 기존 원소보다 크거나 같으면 0으로 남음
#                 c[x][y] += dfs(nx,ny) # 조건에 맞으면 해당 배열에 dfs(새idx들)을 덧셈 연산
#
#     return c[x][y]
#
# m,n = map(int,input().split())
# a = [list(map(int,input().split())) for _ in range(m)]
# c = [[-1]*n for _ in range(m)] # -1로 초기화 하는 이유: 방문했지만 조건에 맞지 않는 경우를 0으로 두기 위함
# print(dfs(0,0))
# for i in range(len(c)):
#     print(c[i])


# 다시풀어보기
# - dfs로 푼다.
# - 현재 값보다 작은 곳으로만 간다.
# - 재귀로 들어가면서, m, 위치에 도달하면 1을 반환한다.
# - 그런식으로 갈 수 있는 경로의 수 반환

# import sys
#
# input = sys.stdin.readline
#
# m, n = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(m)]
# dp = [[-1 for _ in range(n)] for _ in range(m)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def dfs(x, y):
#     global cnt
#     if x == m - 1 and y == n - 1:
#         cnt += 1
#         return 1
#     dp[x][y] = 0
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < m and 0 <= ny < n \
#                 and matrix[x][y] > matrix[nx][ny] and dp[nx][ny] == -1:
#             dp[x][y] = max(dp[x][y], dfs(nx, ny))
#     dp[x][y] += 1
#     return dp[x][y]
#
# cnt = 0
# print(max(0, dfs(0, 0)))
#
# print('\n'+str(cnt))

## 참고
# 확인할 거
# - bfs로 가능한 경로 다확인하기인데, 이미 저장된 값 0이면 0을 반환하는 건 뭐??
# - 전반적으로 모르겠다

# import sys
#
# input = sys.stdin.readline
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# m, n = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(m)]
# dp = [[-1 for _ in range(n)] for _ in range(m)]
#
# def dfs(x, y):
#     if x == m - 1 and y == n - 1:
#         return 1
#     if dp[x][y] != -1:
#         return dp[x][y]
#     dp[x][y] = 0
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < m and 0 <= ny < n:
#             if matrix[nx][ny] < matrix[x][y]:
#                 dp[x][y] += dfs(nx, ny)
#     return dp[x][y]
#
#
# print(dfs(0, 0))
# for i in range(len(dp)):
#     print(dp[i])
    
    
# - dfs
# - 가능한 배열방을 깊이 우선탐색으로 방문
# - 맨 끝에 도달하면 다시 뒤돌아오면서
# - 방문했던 배열방에 더하기 연산
# - m,n을 찍은 횟수가 0,0에 저장되게 된다


# 다시 해보기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
m,n = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)] # 방문 체크와 카운트를 함께 하기 위해 -1로 초기화

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and matrix[x][y] > matrix[nx][ny]:
            dp[x][y] += dfs(nx,ny)
    return dp[x][y]

print(dfs(0,0))