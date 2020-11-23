# 포도주 시식

# 10 + 13 + 8 + 1 = 23 + 9 = 32
# 6 + 10  + 9 + 8 = 16 + 17 = 33

# 포도주 배열
# w = []

# 1차(32나옴)
# import sys
# input = sys.stdin.readline
# N = int(input())
# w = [0]
# for i in range(N):
#     w.append(int(input()))
#
# # print(w)
#
# dp = [0]*10001
# dp[1]=w[1]
# if N > 1:
#     dp[2]=w[1]+w[2]
#
#     for i in range(1,N+1):
#         dp[i] = max(dp[i-3]+w[i-1],dp[i-2])+w[i]
#
# print(dp)
# print(dp[N])

# 2차 (반드시 마지막 잔을 마실 필요가 없으므로) ==> 틀림
# import sys
# input = sys.stdin.readline
# N = int(input())
# w = [0]
# for i in range(N):
#     w.append(int(input()))
#
# # print(w)
#
# dp = [0]*10001
# dp[1]=w[1]
# if N > 1:
#     dp[2]=w[1]+w[2]
#
#     for i in range(1,N+1):
#         dp[i] = max(dp[i-3]+w[i-1],dp[i-2])+w[i]
#
# print(max(dp))

# 3차 (틀림)
# import sys
# input = sys.stdin.readline
# N = int(input())
# w = [0]*10001
# for i in range(1,N+1):
#     w[i] = int(input())
#
# dp = [0]*10001
# dp[1]=w[1]
# if N > 1:
#     dp[2]=w[1]+w[2]
#
#     for i in range(3,N+1):
#         dp[i] = max(dp[i-3]+w[i-1],dp[i-2])+w[i]
#
# print(max(dp))

# 4차 (틀려)
# import sys
# input = sys.stdin.readline
# N = int(input())
# w = [0]*10001
# for i in range(1,N+1):
#     w[i] = int(input())
#
# dp = [0]*10001
# dp[1]=w[1]
# dp[2]=w[1]+w[2]
# dp[3]=max(dp[1],dp[2])+w[3]
#
# if N > 3:
#     for i in range(4,N+1):
#         dp[i] = max(dp[i-3]+w[i-1],dp[i-2])+w[i]
#
# print(max(dp))

# 5차
# import sys
# input = sys.stdin.readline
# N = int(input())
# w = [0]*10001
# for i in range(1,N+1):
#     w[i] = int(input())
#
# dp = [0]*10001
# dp[1]=w[1]
# dp[2]=w[1]+w[2]
# dp[3]=max(dp[1],dp[2])+w[3]
#
# if N > 3:
#     for i in range(4,N+1):
#         dp[i] = max(dp[i-1],dp[i-3]+w[i-1],dp[i-2])+w[i]
#
# print(max(dp))

# 6차
# import sys
# input = sys.stdin.readline
# N = int(input())
# w = [0]*10001
# for i in range(1,N+1):
#     w[i] = int(input())
#
# dp = [0]*10001
# dp[1]=w[1]
# dp[2]=w[1]+w[2]
# dp[3]=max(dp[1],dp[2])+w[3]
#
# if N > 3:
#     for i in range(4,N+1):
#         dp[i] = max(dp[i-1],dp[i-3]+w[i-1],dp[i-2])+w[i]
#
# print(dp[N])

# 7차 (반례 보기) ==> 성공 (50m)
# 6
# 1000 1000 1 1 1000 1000
import sys
input = sys.stdin.readline
N = int(input())
w = [0]*10001
for i in range(1,N+1):
    w[i] = int(input())

dp = [0]*10001
dp[1]=w[1]
dp[2]=w[1]+w[2]
dp[3]=max(dp[2],w[1]+w[3],w[2]+w[3])

if N > 3:
    for i in range(4,N+1):
        dp[i] = max(dp[i-1],dp[i-3]+w[i-1]+w[i],dp[i-2]+w[i])

print(dp[N])