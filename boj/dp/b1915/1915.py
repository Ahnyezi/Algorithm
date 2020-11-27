# 가장 큰 정사각형 (별 두개- 방법)
# - bfs

## 정사각형이 아니다.
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# n,m = map(int,input().split())
# arr = [list(map(int,input().rstrip())) for _ in range(n)]
# dp = [[0 for _ in range(m)] for _ in range(n)]
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# def bfs(i,j):
#     queue = deque([[i,j]])
#     dp[i][j] = 1
#     mv = dp[i][j] # 최대값
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m and \
#                     arr[nx][ny] == 1 and dp[nx][ny] == 0:
#                 dp[nx][ny] = dp[x][y] + 1
#                 queue.append([nx,ny])
#                 mv = max(mv,dp[nx][ny])
#     return mv
#
# max_value = 0
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == 1 and dp[i][j] == 0:
#             max_value = max(max_value,bfs(i,j))
#
# for i in range(len(dp)):
#     print(dp[i])
# print(max_value)

# 참고
# n,m = map(int,input().split())
#
# data = []
#
# for i in range(n):
#     s = input()
#     data.append(list(map(int,list(s))))
#
# dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
# side = 0
#
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if data[i-1][j-1] == 1:
#             dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
#
#             if dp[i][j] > side:
#                 side = dp[i][j]
#
# print(side**2)

## 다시 짜보기
# - 정사각형을 구하는 것이기 때문에 bfs로 처리하는 것이 아니다.
# - dp : 이중 for 문을 이용해서 현재 인덱스에서 가질 수 있는 정사각형 최대변의 길이를 구한다.
#    - 만약 현재 있는 칸이 1이고, 인덱스가 i,j라고 할 때
#    - 정사각형을 이룰 수 있는 연관 인덱스들을 방문하여
#    - 현재 위치에서 정사각형 최대변의 길이를 dp 방에 삽입한다.
#       - (연관 인덱스) i,j-1/i-1,j-1/i-1,j
#       - '정사각형'을 만들어야 하기 때문에
#       - 3개 배열방의 최소값(모든 배열방을 고려했을 때 만들 수 있는 최소 정사각형의 변 길이) +1 값을 현재 배열방에 넣어준다.
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
matrix = [list(map(int,list(input().rstrip()))) for _ in range(n)]
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

length = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if matrix[i-1][j-1] == 1:
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
            if dp[i][j] > length:
                length = max(length, dp[i][j])

print(length**2)
