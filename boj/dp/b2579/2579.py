# 계단 오르기
# 점수 최댓값 구하기

# 규칙
# 계단은 한번에 1칸 혹은 2칸 오를 수 있음 d[n] = d[n-1] + d[n-2]
# 연속된 세 계단을 모두 밟을 수 없다.
# 시작점은 계단에 포함되지 않는다
# 마지막 도착 계단은 반드시 밟아야 한다. (도착점은 계단에 포함)
# 계단의 개수는 300이하의 자연수

# 예시 분석
# 10 20 15 25 10 20
# d[0]= 0
# d[1] = 10 [1]
# d[2] => [1,2] = 30 or [2] = 20
# d[3] => d[1]에서 2칸 or d[2]에서 1칸
# [1,2,3](x) [1,3] = 25 or [2,3] = 35
# d[4] = d[2]에서 2칸 or d[3]에서 1칸
# d[2]에서 올라온 경우

# 다른 의사코드로
# 1,2,4,6
# 일단, 1칸2칸 올라갈 수 있다는 규칙으로 점화식 세워서 구하기
# 구한 값이 연속 3개 수 있을 경우 제외
# 마지막 도착 계단 안밟은 경우 제외

# import sys
# input = sys.stdin.readline
# N = int(input())
# points = [0]
# for _ in range(N):
#     points.append(int(input()))
# used = []
# d = [0]*(N+1)
# d[1] = points[1]
# for i in range(2,N+1):
#     if d[i-1]< d[i-2]:
#         d[i] = d[i-2] + points[i]
#         u = i-2
#     elif d[i-1]> d[i-2]:
#         d[i] = d[i-1] + points[i]
#         u = i - 1
#     else:
#         pass
#     if len(used) == 3:
#         used.pop(0)
#     used.append(u)

# 몰게떠

# 2차시도(런타임 에러)
# 조건이 있는 경우에도 점화식을 세우는 데에 집중하기
# 1) 연속하는 3 수 조건 없을 경우 점화식
# d(n) = max(d(n-1) + points[n], d(n-2)+points[n])
# 2) 연속하는 3 수 조건 적용할 경우 점화식 ==> 모든 조건 cover 가능
# d(n) = max(d(n-3) + points[n-1] + points[n], d(n-2)+points[n])

import sys
input = sys.stdin.readline
N = int(input())
points = [0] * (N+1)
for i in range(1,N+1):
    points[i] = int(input())

d = [0]*(N+1)
d[1] = points[1]
d[2] = max(d[1]+points[2],points[2])

for i in range(3,N+1):
    d[i] = max(d[i-3]+points[i-1]+points[i],d[i-2]+points[i])

print(d[N])


## 문제점 : 방 301개로 안만들어줘서!!!!

# import sys
# input = sys.stdin.readline
# N = int(input())
# points = [0] * 301 ##
# for i in range(1,N+1):
#     points[i] = int(input())
#
# d = [0]*301 ##
# d[1] = points[1]
# d[2] = max(d[1]+points[2],points[2])
#
# for i in range(3,N+1):
#     d[i] = max(d[i-3]+points[i-1]+points[i],d[i-2]+points[i])
#
# print(d[N])

## N+2
import sys
input = sys.stdin.readline
N = int(input())
points = [0] * (N+2)
for i in range(1,N+1):
    points[i] = int(input())

d = [0]*(N+2)
d[1] = points[1]
d[2] = max(d[1]+points[2],points[2])

for i in range(3,N+1):
    d[i] = max(d[i-3]+points[i-1]+points[i],d[i-2]+points[i])

print(d[N])

#### 안봐도 돼

# 3차시도(틀림)

# import sys
# input = sys.stdin.readline
# N = int(input())
# points = [0]
# for _ in range(N):
#     points.append(int(input()))
# print(points)
#
# d = [0]*(N+1)
# d[1] = points[1]
# d[2] = max(d[1]+points[2],points[2])
# d[3] = max(d[2]+points[3],d[1]+points[3])
#
# for i in range(4,N+1):
#     d[i] = max(d[i-3]+points[i-1]+points[i],d[i-2]+points[i])
#
# print(d)
#
# print(d[N])

# 4 (오답)
# import sys
# input = sys.stdin.readline
# N = int(input())
# points = [0] * 301
# for i in range(1,N+1):
#     points[i] = int(input())
#
# d = [0] * 301
# d[1] = points[1]
# d[2] = max(d[1]+points[2],points[2])
# d[3] = max(d[2]+points[3],d[1]+points[3])
#
# for i in range(4,N+1):
#     d[i] = max(d[i-3]+points[i-1]+points[i],d[i-2]+points[i])
#
# print(d[N])

# 5 (오답)
# import sys
# input = sys.stdin.readline
# N = int(input())
# points = [0 for i in range(301)]
# for i in range(1,N+1):
#     points[i] = int(input())
#
# d = [0 for i in range(301)]
# d[1] = points[1]
# d[2] = max(d[1]+points[2],points[2])
# d[3] = max(d[2]+points[3],d[1]+points[3])
#
# for i in range(4,N+1):
#     d[i] = max(d[i-3]+points[i-1]+points[i],d[i-2]+points[i])
#
# print(d[N])

# 6 (오답)
# import sys
# input = sys.stdin.readline
# N = int(input())
# points = [0 for i in range(301)]
# for i in range(1,N+1):
#     points[i] = int(input())
#
# d = [0 for i in range(301)]
# d[1] = points[1]
# d[2] = d[1]+points[2]
# d[3] = max(d[2]+points[3],d[1]+points[3])
#
# for i in range(4,N+1):
#     d[i] = max(d[i-3]+points[i-1]+points[i],d[i-2]+points[i])
#
# print(d[N])

# 7
# N = int(input())
# points = [0 for i in range(301)]
# for i in range(1,N+1):
#     points[i] = int(input())
#
# d = [0 for i in range(301)]
# d[1] = points[1]
# d[2] = d[1]+points[2]
# d[3] = max(d[2]+points[3],d[1]+points[3])
#
# for i in range(4,N+1):
#     d[i] = max(d[i-3]+points[i-1]+points[i],d[i-2]+points[i])
#
# print(d[N])

# 8 (정답 ==> d[3]항 오류)
# n = int(input())
# points = [0 for i in range(301)]
# d = [0 for i in range(301)]
#
# for i in range(1,n+1):
#     points[i] = int(input())
#
# d[1] = points[1]
# d[2] = points[1]+points[2]
# d[3] = max(points[2]+points[3],points[1]+points[3])
#
# for i in range(4,n+1):
#     d[i] = max(d[i-3]+points[i-1]+points[i],d[i-2]+points[i])
#
# print(d[n])
