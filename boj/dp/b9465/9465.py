# 스티커
# 여태까지랑 다른 방법

# dp[0][1] += dp[1][0]
# dp[1][1] += dp[0][0]
# 초기 세팅

# dp[0][j] += max(dp[1][j-1],dp[1][j-2])
# dp[1][j] += max(dp[0][j-1],dp[0][j-2])
# 점화식

import sys
input = sys.stdin.readline
T =int(input())
for _ in range(T):
    n = int(input())
    dp = []
    for _ in range(2):
        dp.append(list(map(int,input().split())))

    if n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    for i in range(2,n):
        dp[0][i] += max(dp[1][i-1],dp[1][i-2])
        dp[1][i] += max(dp[0][i-1],dp[0][i-2])

    print(max(dp[0][-1],dp[1][-1]))


