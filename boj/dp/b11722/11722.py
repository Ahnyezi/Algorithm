# 가장 긴 감소하는 부분 수열
# 각 idx마다 idx+1부터 끝까지 순회하며
# nums[idx]보다 작은 nums방의 가장 큰 값을 붙인 수열 생성

# https://www.acmicpc.net/problem/11722
## 1차 (시간 초과)
# import sys
# input = sys.stdin.readline
# N = int(input())
# sequence = list(map(int,input().split()))
# dp = [0]*N
#
# for i in range(N):
#     s = [sequence[i]]
#     for _ in range(N-i): # 3) 1,2번을 남은 칸 수만큼 시행
#         max_value = 0
#         for j in range(i+1,N): # 1) 현재 값보다 작은 값 중 가장 큰 값 구함
#             if sequence[j] < s[-1]:
#                if sequence[j] > max_value:
#                    max_value = sequence[j]
#         if max_value != 0:
#             s.append(max_value) # 2) 존재한다면, s에 삽입
#     # print(str(i),'의 s:',s)
#     dp[i] = len(s)
#
# # print(dp)
# print(max(dp))

## 2차(참고)
import sys
input = sys.stdin.readline
N = int(input())
sequence = list(map(int,input().split()))
dp = [1 for i in range(N)]

for i in range(1,N): # i번째 자리에서 비교
    s = []
    for j in range(i):
        if sequence[i] < sequence[j]: # i 이전의 값들 중 sequence[i]보다 큰 수 sequence[j]를 찾으면
            s.append(dp[j]) # dp j번째 항을 s에 삽입 [j번째 값의 수열길이]
    if not s:
        continue
    else:
        dp[i] += max(s)
print(max(dp))