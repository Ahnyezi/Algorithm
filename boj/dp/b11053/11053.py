# 가장 긴 증가하는 부분 수열

# 1차 (예제 틀림)
# import sys
# input = sys.stdin.readline
# N = int(input())
# A = list(map(int,input().split()))
#
# print(A)
#
# dp = [0]*1000
# dp[0] = 1
# for i in range(1, N):
#     prev = 0
#     dp[i] = dp[i-1]
#     for j in range(i):
#         if prev < A[j]:
#             dp[i] += 1
#             prev = A[j]
#
# print(dp)
# print(dp[N])

# 2차 (예제 맞, 틀림)
# import sys
# input = sys.stdin.readline
# N = int(input())
# A = list(map(int,input().split()))
# 
# dp = [0]*1000
# dp[0] = 1
# for i in range(1, N):
#     prev = 0
#     for j in range(i+1):
#         if prev < A[j]:
#             dp[i] += 1
#             prev = A[j]
# print(dp[N-1])


# 3차시도
# 4
# 1 4 2 3
# import sys
# input = sys.stdin.readline
# N = int(input())
# A = list(map(int,input().split()))
#
# dp = [0]*1000
# dp[0] = 1
# for i in range(1, N): # i: DP 삽입 idx
#     prev = 0
#     for j in range(i+1): # j: 배열 A idx
#         for k in range(j): # k : 배열 A의 j 전까지 (prev 배열)
#             if A[k] < A[j]:
#                 dp[i] += 1
#                 # prev = A[j]
# print(dp[N-1])

# 4차 (반례는 맞았지만, 원래 예제 조건 틀림)
# - 해당 idx의 수보다 적은 수를 가진 항이 몇개인지 dp에 저장
# import sys
# input = sys.stdin.readline
# N = int(input())
# A = list(map(int,input().split()))
#
# dp = [1]*1000
# for i in range(1, N): # i: DP 삽입 idx
#     for j in range(i):
#         if A[i] > A[j]: # 현재항보다 작은수를 가진 경우
#             dp[i] += 1
# print(dp[N-1])

# 5차 (시간 초과)
# - DP 삽입 IDX
# - 현재방 이전의 배열들을 방문
# - 포함/미포함 수인지 검사하여 현재 dp 방에 +1
# import sys
# input = sys.stdin.readline
# N = int(input())
# A = list(map(int,input().split()))
#
# dp = [1]*1000
# for i in range(1, N): # i: DP 삽입 idx
#     for j in range(i): # j: 현재 배열방 이전의 배열들 확인
#         if A[i] > A[j]: # 현재항보다 작은수를 가진 경우
#             flag = True
#             for k in range(j): # 이미 포함된 수인지 검사
#                 if A[k] == A[j]:
#                     flag = False
#             if flag: # 이전에 없는 수일 경우에만 더해줌
#                 dp[i] += 1
# print(dp[N-1])

# 6차 (다른 답안 참고)
# - 자기자신보다 작은 숫자들 중 가장 큰 길이를 구하고
# - 그 길이에 +1을 한다
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
dp = [0] * N
for i in range(N):
    for j in range(i):# 0~i-1
        # 1) 현재항보다 작은 수
        # 2) 최대의 DP 값 가진 배열방
        if A[j] < A[i] and dp[j] > dp[i]: 
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))

# 7차 (오답과 반례)
# - 조건: 자기보다 작은수이면서 최대길이인 항 +1
# - 따라서 최대값이 존재하는 idx의 dp값이 최대임
# 5
# 1 2 3 1 2 
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
dp = [0] * N
for i in range(N):
    for j in range(i):# 0~i-1
        # 1) 현재항보다 작은 수
        # 2) 최대의 DP 값 가진 배열방
        if A[j] < A[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1
print(dp) # [1, 2, 3, 1, 2]
print(dp[N-1]) # 2 (3이어야 함)