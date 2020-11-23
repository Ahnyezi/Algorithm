# 카드 구매하기
# Pi=x원 ==> 카드 i개가 들어있는 카드팩의 가격은 x원
# P1=1,P2=5,P3=6,P4=7일때, 카드 4개 갖게 하는 최대가격 == 10 (P2*2)
# 몫: 4/2/1+3/1
# 4       10     7     7
# 딱 떨어지는 경우만 가능

## 1차 (틀림)
# import sys
# input = sys.stdin.readline
# N = int(input())
# packs = [0] + list(map(int,input().split()))
# dp = [0 for _ in range(len(packs))]
#
# for i in range(1,len(packs)):
#     remainder = N % i
#     print('i:',str(i))
#     print('remainder:',end='')
#     print(remainder)
#     if remainder == 0: # 나머지 없음
#         dp[i] = packs[i] * (N // i)
#     else: # 나머지 있음
#         for j in range(len(packs)):
#             if remainder == j:
#                 dp[i] = packs[i] * (N // i) + packs[j]
#                 # dp[i] = packs[i] * (packs[i] // N) + packs[j]
#
# print(dp)
# print(max(dp))

# - 반례
# 10
# 카드개수: 1  2   3  4 5 6 7 8 9 10
# answer: 520
# 기존의 알고리즘 대로 할 경우
# 팩의가격: 1 100 160 1 1 1 1 1 1 1
# 살 개수 :10  5  3   2 2 1 1 1 1 1
# 나머지  :       1   2   4 3 2 1
# 총합  :10/500/481/102/2/2/161/101/2/1 =>500

## 2차 (알고리즘 참고)
# - <생각의 전환> **
# - 최댓값을 구해야 하므로, 모든 경우를 다 세어봐야 함
# - (예) n=10일때,
# - 기존에 생각한 방법: (0,10) (1,9) (2,8) (3,7)...
# - 실제 경우의 수들 :  (1,1,1,1,6), (2,2,6), (4,6) 중 가장 큰 값...

import sys
input = sys.stdin.readline
N = int(input())
price = [0] + list(map(int,input().split()))
dp = [0]*(N + 1)
dp[1] = price[1]

for i in range(2,N+1):
    for j in range(1,i+1):
        if dp[i] < dp[i-j] + price[j]:
            dp[i] = dp[i-j] + price[j]

print(dp[N])

