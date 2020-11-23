# 정수삼각형
# 삼각형의 크기와 각 삼각형의 숫자가 주어짐
# 합이 최대가 되는 경로에 있는 합 출력
# 아래로 내려올 때, 자기 인덱스나 자기 인덱스 +1에만 접근 가능

# 1차시도 (29m)
# import sys
# input = sys.stdin.readline
# N = int(input())
# square = [0]
# for i in range(1,N+1):
#     s = input()
#     if ' ' in s:
#         ss = s.split(' ')
#         ns = list(map(int,ss))
#         square.append(ns)
#     else:
#         square.append(int(s))
#
# d = [0,square[1]]
# idx = 0
# for i in range(2,N+1):
#     if square[i][idx] <= square[i][idx+1]:
#         d.append(d[i-1]+square[i][idx+1])
#         idx += 1
#     elif square[i][idx] > square[i][idx+1]:
#         d.append(d[i-1]+square[i][idx])
#
# print(d[-1]) # 28

# 모든 경우 고려하지 않고
# 현 시점에서 가장 큰 경우 따라감.


# 2차시도 (예제를 다시 보자)
# DP를 2차원으로 생성하여 모든 경우를 고려하기
# 각 자리에 올 수 있는 최대값을 저장하는 2차원 배열 DP
# 각 라인의 끝자리에 있는 경우가 아니라면, 경우의 수 2가지
# 중간에 있는 경우에만 MAX 함수로 최댓값을 넣어준다.

# import sys
# input = sys.stdin.readline
# N = int(input())
# square = [0]
# for i in range(1,N+1):
#     s = input()
#     if i == 1:
#         square.append(int(s))
#     else:
#         ss = s.split(' ')
#         ns = list(map(int,ss))
#         square.append(ns)
#
# # print(square)
# dp = [0]*500
#
# for i in range(1,N+1):
#     for j in range(i):
#         pass

# 몰르게쏘

# 3차시도(답안 참고)
# - square 자체가 dp 배열이 되게 해라

import sys
input = sys.stdin.readline
N = int(input())
dp = []
for i in range(N):
    dp.append(list(map(int,input().split())))

for i in range(1,N):
    for j in range(i+1):
        if i == 1:
            dp[1][j] += dp[0][0]
        else:
            if j == 0:
                dp[i][0] += dp[i-1][0]
            elif j == i:
                dp[i][i] += dp[i-1][i-1]
            else:
                dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])

max = dp[N - 1][0]
for i in range(1,N):
    if dp[N-1][i] > max:
        max = dp[N-1][i]

print(max)