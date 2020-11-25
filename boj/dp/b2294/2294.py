# 동전2
# - n가지 동전을 사용하여 k원을 만든다
# - 각 종류의 동전은 무제한으로 사용 가능
# - 최소로 사용할 수 있는 동전개수를 출력하라. / 안되면 -1
# - 동전은 같은 것이 여러 번 주어질 수 있음

# import sys
# input = sys.stdin.readline
# n,k = map(int,input().split())
# coins = []
# for _ in range(n):
#     coins.append(int(input()))
# coins = [0] + sorted(list(set(coins)))
#
# dp = [[0 for _ in range(k+1)] for _ in range(len(coins)+1)]
#
# for i in range(coins[1],k+1,coins[1]):
#     dp[1][i] = i // coins[1]
#
# for i in range(2,len(coins)):
#     print('c:',coins[i])
#     dp[i][coins[i]] = 1
#     for j in range(coins[i],k+1,coins[i]):
#         dp[i][j] = dp[i-1][j] - coins[i] * (j // coins[i]) + j // coins[i]
#     for k in range(len(dp)):
#         print(dp[k])import sys
# input = sys.stdin.readline
# n,k = map(int,input().split())
# coins = []
# for _ in range(n):
#     coins.append(int(input()))
# coins = [0] + sorted(list(set(coins)))
#
# dp = [[0 for _ in range(k+1)] for _ in range(len(coins)+1)]
#
# for i in range(coins[1],k+1,coins[1]):
#     dp[1][i] = i // coins[1]
#
# for i in range(2,len(coins)):
#     print('c:',coins[i])
#     dp[i][coins[i]] = 1
#     for j in range(coins[i],k+1,coins[i]):
#         dp[i][j] = dp[i-1][j] - coins[i] * (j // coins[i]) + j // coins[i]
#     for k in range(len(dp)):
#         print(dp[k])

## 1차 틀렷대 ;;
# import sys
# input = sys.stdin.readline
# n,k = map(int,input().split())
# coins = []
# for _ in range(n):
#     coins.append(int(input()))
# coins = [0] + sorted(list(set(coins)))
#
# dp = [[0 for _ in range(100001)] for _ in range(len(coins))]
#
# for i in range(coins[1],k+1,coins[1]):
#     dp[1][i] = i // coins[1]
#
# for i in range(2,len(coins)):
#     dp[i][coins[i]] = 1
#     for j in range(1,k+1):
#         if j % coins[i] == 0:
#             dp[i][j] = dp[i-1][j] - coins[i] * (j // coins[i]) + j // coins[i]
#         else:
#             dp[i][j] = dp[i-1][j]
#
# ans = dp[len(coins)-1][k]
# if ans == 0:
#     print(-1)
# else:
#     print(dp[len(coins)-1][:k+1])
#     print(ans)

# 참고
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

# dp = [-1 for _ in range(k+1)]
# 초장부터 -1로 놓게 되면 이중 for문 안에 조건문에 단 한번도 안들어감
dp = [10001 for _ in range(k+1)]
# 10001로 설정한 이유?
# 조건문 if dp[j] > dp[j-coins[i]] + 1:로 값을 넣어주기 위해서는

dp[0] = 0
print(dp)

for i in range(n):
    for j in range(coins[i],k+1):
        if dp[j] > dp[j-coins[i]] + 1:
            dp[j] = dp[j-coins[i]] + 1 # 그 전시행에서 구해진 값 + 1
                                        # ex) dp[10] = dp[10-coins[1]] + 1
                                        #            = dp[10- 5] + 1
                                        #            = dp[5] + 1
                                        #            = 1 + 1
    print(dp)

print(dp[k])
# if dp[k] == 10001:
#     print(-1)
# else:
#     print(dp[k])