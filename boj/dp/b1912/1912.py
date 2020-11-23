# 연속합
# 연속된 몇 개의 수를 선택해서 합이 가장 큰 합 구하기

# 1차
# import sys
# input = sys.stdin.readline
# N = int(input())
# seq = list(map(int,input().split()))
#
# dp = [0] * 100001
# dp[1] = seq[0]
#
# if N > 1:
#     for i in range(2,N+1):
#         dp[i] = max(dp[i-1],seq[i-2]+seq[i-1],seq[i-1])
#
# print(dp) # 예제 충족 못시킴

# 2차
import sys
input = sys.stdin.readline
N = int(input())
seq = list(map(int,input().split()))

dp = [0] * 100001
dp[1] = seq[0]

if N > 1:
    for i in range(2,N+1):
        dp[i] = max(dp[i-1]+seq[i-1],seq[i-2]+seq[i-1],seq[i-1])

answer = max(dp)
if answer == 0:
    answer = dp[1]
    for i in range(1,N+1):
        if dp[i] == 0:
           answer = 0
           break
        else:
            if dp[i] > answer:
                answer = dp[i]

print(answer)