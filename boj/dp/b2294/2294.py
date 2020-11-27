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

# 다시 풀어보자
# n개의 동전이 주어지며, 각 라인에 해당 동전의 가치가 주어진다.
# 해당 동전들을 최소로 사용하여 가치가 k원이 되도록 해라

## 틀렷다 ㅎ
# import sys
# input = sys.stdin.readline
# n,k = map(int,input().split())
# coins = [0]
# for _ in range(n):
#     coins.append(int(input().rstrip()))
#
# dp = [0 for _ in range(10001)]
#
# for i in range(1,len(coins)):
#     dp[coins[i]] = 1
#     for j in range(coins[i]+1,k+1):
#         if dp[j-coins[i]] != 0:
#             dp[j] = dp[j-coins[i]] + 1
#         else:
#             dp[j] = dp[j-1] + 1
#     print(dp)
#
# if dp[k] == 0:
#     print(-1)
# else:
#     print(dp[k])

## 참고해서 다시 풀이
# n개의 동전으로 k원을 만들 때, k원을 만들 수 있는 최소 동전 개수를 return 한다
# 동전의 개수만큼 반복하면서, dp각 방에 (idx)원을 만들 수 있는 최소 개수를 연산해 나간다.
# > 점화식은 다음과 같이 세울 수 있다.
# dp[j] = dp[j-coins[i]] + 1
# `dp[j]`: j 가치를 만들 수 있는 최소 동전의 개수는
# `dp[j-coins[i]]`: (현재 가치 - 현재 사용 동전 가치)를 만들 수 있는 최소 동전의 개수 + 1
# > 해당 점화식을 모든 경우에 사용할 수는 없다.
# 모든 동전을 사용해도 만들 수 없는 가치가 있으며,
# 이런 경우, 위의 점화식으로 해당 방의 값이 초기화 되어서는 안된다.
# 이런 경우를 처리하기 위하여
# 우선 dp 배열 모든 방의 값을 k의 가용범위에서 넘어서는 숫자인 10001로 초기화한다.
# 그런 뒤에, 위에서 세워 놓은 점화식을 실행하는 조건을
# if dp[j] > dp[j-coins[i]] + 1: 로 둔다.
# 이 말은, j라는 인덱스의 배열방(j 가치를 만들기 위한 최소 동전 개수)가
# 현재의 동전으로 재연산 한 후의 값 (dp[j-coins[i]] + 1) 보다 클 경우에만 실행되며,
# 만약 j-coins[i]라는 값의 방이 10001 즉, 어떠한 동전으로도 만들 수 없는 가치라면
# 해당 점화식을 사용할 수 없기 때문에 조건에 충족되지 않고 다음으로 넘어가게 된다.


import sys
input = sys.stdin.readline
n,k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input().rstrip()))
dp = [10001 for _ in range(k+1)]
dp[0] = 0 # 점화식 사용을 위한 0번째 배열방 setting

for i in range(n):
    for j in range(coins[i],k+1):
        if dp[j] > dp[j-coins[i]] + 1:
            dp[j] = dp[j-coins[i]] + 1

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])



