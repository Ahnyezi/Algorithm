# 답안

# n = int(input())
# s = [0 for i in range(301)]
# dp = [0 for i in range(301)]
# for i in range(n):
#     s[i] = int(input())
# dp[0] = s[0]
# dp[1] = s[0] + s[1]
# dp[2] = max(s[1] + s[2], s[0] + s[2])
# for i in range(3, n):
#     dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
# print(dp[n - 1])

# 오답

# n = int(input())
# s = [0 for i in n+1]
# dp = [0 for i in n+1]
# for i in range(n):
#     s[i] = int(input())
# dp[0] = s[0]
# dp[1] = s[0] + s[1]
# dp[2] = max(s[1] + s[2], s[0] + s[2])
# for i in range(3, n):
#     dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
# print(dp[n - 1])

# 정답
# n = int(input())
# s = [0 for i in range(301)]
# dp = [0 for i in range(301)]
# for i in range(n):
#     s[i] = int(input())
# dp[0] = s[0]
# dp[1] = s[0] + s[1]
# dp[2] = max(s[1] + s[2], s[0] + s[2])
# for i in range(3, n):
#     dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
# print(dp[n - 1])

# 정답
n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(1,n+1):
    s[i] = int(input())
dp[1] = s[1]
dp[2] = s[1] + s[2]
dp[3] = max(s[2] + s[3], s[1] + s[3])
for i in range(4, n+1):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n])
