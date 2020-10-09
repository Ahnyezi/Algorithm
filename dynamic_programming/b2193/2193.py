# 이친수

# 1차시도 (모르겟어)

# 의사코드
# - 앞의 배열에서 +0, +1을 한 결과를 모든 배열에 넣고
# 각 항을 검사하여 조건에 맞는 것만 count

# import sys
# input = sys.stdin.readline
# N = int(input())
#
# def check(s):
#     print('test:'+s)
#     if s[0] == '0':
#         return False
#     if '11' in s:
#         return False
#     return True
#
# dp =[]
# for i in range(1,N+1):
#     dp.append([0]*i)
#
# dp[0][0] = '1'
# for i in range(1,N+1):
#     print('i:'+str(i))
#     for j in range(len(dp[i-1])):
#         if check(str(dp[i-1][j])+'0'):
#             print('성공:'+str(dp[i-1][j])+'0')
#         elif check(str(dp[i-1][j])+'1'):
#             print('성공:'+str(dp[i-1][j])+'1')
#
# print(dp)

# 2차시도(답안 참고) => 런타임 에러

# 의사코드
# - 각 시행을 직접 나열해서 규칙을 찾는다
# - 모든 시행은 전시행 + 0, 전전시행 + 10이라는 규칙을 가짐
# - 이것을 토대로 점화식을 세우면,
# - dp[n] = dp[n-1]+dp[n-2]

import sys
input = sys.stdin.readline
N = int(input())

dp = [0]*90
dp[0] = 1
dp[1] = 1

for i in range(2,N+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[N-1])

# 3차시도 (배열방 개수 잡아줌)
import sys
input = sys.stdin.readline
N = int(input())

dp = [0]*91
dp[0] = 1
dp[1] = 1

for i in range(2,N+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[N-1])