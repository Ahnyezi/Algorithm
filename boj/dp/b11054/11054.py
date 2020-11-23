# 가장 긴 바이토닉 부분 수열

# 1차 (잘못 생각했다)
# - idx에서 가장 긴 증가하는 수열 리스트
# - idx에서 가장 긴 감소하는 수열 리스트를 구한 뒤
# - 더하여 바이토닉 부분 수열을 구한다.
# import sys
# input = sys.stdin.readline
# N = int(input())
# A = list(map(int,input().split()))
# dp_inc = [1]*N
# dp_dec = [1]*N
# dp = [0]*N
#
# # 증가 수열
# for i in range(N):
#     print('i:',str(i))
#     s_inc = []
#     for j in range(i):
#         if A[i] > A[j]:
#             s_inc.append(dp_inc[j])
#     if not s_inc:
#         continue
#     else:
#         dp_inc[i] += max(s_inc)
#
# # 감소 수열
# for i in range(N):
#     s_dec = []
#     for j in range(i):
#         if A[i] < A[j]:
#             s_dec.append(dp_dec[j])
#     if not s_dec:
#         continue
#     else:
#         dp_dec[i] += max(s_dec)
#     dp[i] = dp_inc[i] + dp_dec[i] - 1
#
# print(dp_inc)
# print(dp_dec)
# print(dp)
#

## 2차 (성공)
# - 증가 수열 구하고
# - 끝에서부터 감소하는 수열 구해서
# - 바이토닉 수열 구하기
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
dp_inc = [1]*N
dp_dec = [1]*N
dp = [0]*N

# 증가 수열
for i in range(N):
    s_inc = []
    for j in range(i):
        if A[i] > A[j]:
            s_inc.append(dp_inc[j])
    if not s_inc:
        continue
    else:
        dp_inc[i] += max(s_inc)

# 감소 수열
for i in range(N-1,0,-1):
    print(i)
    s_dec = []
    for j in range(N-1,i,-1):
        if A[i] > A[j]:
            s_dec.append(dp_dec[j])
    if not s_dec:
        continue
    else:
        dp_dec[i] += max(s_dec)

for i in range(N):# 감소에 넣으면 if not s_dec에 걸릴 경우 continue되어서 dp값 0으로 남아있음
    dp[i] = dp_inc[i] + dp_dec[i] - 1

print('dp_inc:',dp_inc)
print('dp_dec:',dp_dec)
print('dp:',dp)
print(max(dp))

## 참고
# import sys
# input = sys.stdin.readline
# n = int(input())
# a = list(map(int,input().split()))
# dpp = [0 for i in range(n)]
# dpm = [0 for i in range(n)]
# dpb = [0 for i in range(n)]
#
# # 증가수열 구하기
# for i in range(n):
#     for j in range(i): # i 이전의 값들을 확인
#         if a[i] > a[j] and dpp[i] < dpp[j]:# j번째 값이 i번째 보다 작을 때, dpp[j]는 dpp[i]보다 큰 경우
#             dpp[i] = dpp[j]
#     dpp[i] += 1
# # 감소수열 구하기
# for i in range(n-1,-1,-1):
#     for j in range(n-1,i,-1):
#         if a[i] > a[j] and dpm[i] < dpm[j]:
#             dpm[i] = dpm[j]
#     dpm[i] += 1
# # 바이토닉 수열 구하기
# for i in range(n): #
#     dpb[i] = dpp[i] + dpm[i] - 1
# print(dpp)
# print(dpm)
# print(dpb)
# print(max(dpb))
