# 오르막 수
# 수는 0으로 시작할 수 있다.
# ex) N == 2이면, 01 ~ 99까지
# ex) N == 3이면, 010 ~ 999까지?

# 개별  찐
# 10   10
# 45   55
# 165  220

## 1차 (시간 초과)
# import sys
# N = int(sys.stdin.readline())
# dp = [0] * (N + 1)
# dp[1] = 10
#
# for i in range(2,N+1):
#     cnt = 0
#     for j in range(10**(i-1),10**i):
#         nums = list(str(j))
#         flag = True
#         for k in range(1, len(nums)):
#             if nums[k-1] > nums[k]:
#                 flag = False
#                 break
#         if flag:
#             cnt += 1
#     dp[i] = (dp[i-1] + cnt)  % 10007
#
# print(dp[N] % 10007)

## 2차 시도 (메모리 초과)
# import sys
# N = int(sys.stdin.readline())
# dp = [[0 for _ in range(10**N+1)] for _ in range(10**N+1)]
#
# dp[0][0] = 1
# for i in range(1,10):
#     dp[1][i] = 1
# for i in range(10,100):
#     nums = list(str(i))
#     for j in range(1,len(nums)):
#         if nums[j-1] <= nums[j]:
#             dp[2][i] = 1
# cnt = 55
#
# for i in range(3,N+1): # 3
#     for j in range(10**(i-1),10**i): # 115
#         if str(j)[-2] <= str(j)[-1]: # 1 <= 5
#             if dp[i-1][int(str(j)[:-1])] == 1: # dp[2][11]
#                 dp[i][j] = 1
#                 cnt += 1
#
# print(cnt)

# 정답
import sys
N = int(sys.stdin.readline()) # 자릿수
dp = [[0]*10 for i in range(1001)] # 10 : 끝 자리가 0~9인 숫자의 개수, 1001: 최대 자릿수

for i in range(10): # 자릿수 1개일 때 배열방값 초기화
    dp[1][i] = 1

for i in range(2,1001):
    for j in range(10):
        for k in range(j+1):
            # dp[i][j]: 자릿수가 i이면서 끝자리가 j인 숫자의 개수는
            # dp[i-1][k] : 자릿수가 i-1이면서 끝자리가 j이하인 모든 숫자의 덧셈으로 구한다.
            dp[i][j] += dp[i-1][k] 
            
print(sum(dp[N])%10007)

# i == 1 (10)
# 0 1 2 3 4 5 6 7 8 9
# i == 2 (55)
# 00 01 02 03 04 05 06 07 08 09 10 # 00 들가?
#    11 12 13 14 15 16 17 18 19 9
#       22 23 24 25 26 27 28 29 8
#          33 34 35 36 37 38 39 7
#             44 45 46 47 48 49 6
#                55 56 57 58 59 5
#                   66 67 68 69 4
#                      77 78 79 3
#                         88 89 2
#                            99 1