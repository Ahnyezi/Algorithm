# 퇴사

# 1일째꺼를 한다면
# 1일(10) 4일(20) 5일(15)
# 2일째꺼
# 2일(20)
# 3일째꺼
# 3일(10) 4일(20) 5일(15)
# 4일째꺼
# 4일(20) 5일(15)
# 5일째꺼
# 5일(15)
# 6일째꺼
#
# 7일째꺼
#

## 1차 (모든 경우 고려 안함)
# import sys
# input = sys.stdin.readline
# N = int(input())
# schedule = [0]
# for _ in range(N):
#     schedule.append(list(map(int,input().split())))
# p = [0]*(N+1)
#
# for i in range(1,len(schedule)):
#     j = i
#     profit = 0
#     while j <= N:
#         if j + schedule[j][0] <= N + 1:
#             # print('j:',str(j))
#             profit += schedule[j][1]
#             # print('pro:',str(profit))
#             j += schedule[j][0]
#         else:
#             break
#     p[i] = profit
#     # print()
# print(p)
# print(max(p))


## 2차
# 선택한 날짜의 합이 N+1보다 작을 때
# 뒤에서부터?
# 어떻게 해야 되는지 몰르게따
# import sys
# input = sys.stdin.readline
# N = int(input())
# schedule = [0]
# for _ in range(N):
#     schedule.append(list(map(int,input().split())))
# p = [0]*(N+1)

# 참고1 => 이해 안돼
n = int(input())
t =[]
p = []
dp = []
for i in range(n):
    a,b = map(int,input().split()) # time / profit
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0) # ?
for i in range(n-1,-1,-1):
    if t[i] + i > n: # 퇴사 이후 (이전 시행 dp값 가져옴)
        dp[i] = dp[i + 1]
    else: # 퇴사 이전
        dp[i] = max(dp[i + 1],p[i]+dp[t[i]+i]) # 왜 이렇게 처리해야 돼?
print(dp)
print(dp[0])


# 참고2
# import sys,copy
# input = sys.stdin.readline
# N = int(input()) # 퇴사날짜
# t = [0 for _ in range(N+1)] # 소요일수
# p = [0 for _ in range(N+1)] # 이익
# for i in range(1,N+1):
#     t[i],p[i] = map(int,input().split())
# # 최대 요금 : 각 날짜의 상담을 할 경우 얻을 수 있는 금액으로 초기화
# charge = copy.deepcopy(p)
#
# for i in range(1,N+1):
#     if i + t[i] > N + 1: # 더이상 이동 불가능한 경우
#         charge[i] = 0
#     else:# 이동 가능한 경우
#         for j in range(i+t[i],N+1): # 가능한 모든 경우를 다 따져본다
#             new_charge = charge[i] + p[j]
#             if new_charge > charge[j]:
#                 charge[j] = new_charge
#
# print(max(charge))



