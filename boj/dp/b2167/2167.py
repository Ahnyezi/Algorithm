# 2차원 배열의 합

## 1차 (시간초과) => dp 안씀
# import sys
# input = sys.stdin.readline
#
# N,M = map(int,input().split())
# arr = [0 for _ in range(N+1)]
# for i in range(1,N+1):
#     arr[i] = [0] + list(map(int,input().split()))
#
# K = int(input())
# position = [0]
# for _ in range(K):
#     position.append(list(map(int,input().split())))
#
# for i in range(1,K+1):
#     sum = 0
#     start_x,start_y,end_x,end_y = position[i]
#     for j in range(start_x,end_x+1):
#         for k in range(start_y,end_y+1):
#             sum += arr[j][k]
#     print(sum)

# 2차
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [0 for _ in range(N+1)]
arr[0] = [0 for _ in range(M+1)]
for i in range(1,N+1):
    arr[i] = [0] + list(map(int,input().split()))

# 배열 arr의 0,0부터 i,j 번째까지 원소 합
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = arr[i][j] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

K = int(input())
for _ in range(K):
    i1,j1,i2,j2 = map(int,input().split())
    print(dp[i2][j2]-dp[i1-1][j2]-dp[i2][j1-1]+dp[i1-1][j1-1])

