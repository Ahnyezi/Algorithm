# 내려가기

## 메모리 초과
# import sys
# sys.setrecursionlimit(10**9)
#
# input = sys.stdin.readline
#
# n = int(input())
# matrix = []
# for _ in range(n):
#     matrix.append(list(map(int, input().split())))
# d = [[[1, 0], [1, 1]], [[1, -1], [1, 0], [1, 1]], [[1, -1], [1, 0]]]
#
#
# def dfsmax(x, y):
#     if x == n - 1:
#         return matrix[x][y]
#     res_max = 0
#     nd = d[y]
#     for i in range(len(nd)):
#         nx = x + nd[i][0]
#         ny = y + nd[i][1]
#         res_max = max(res_max, dfsmax(nx, ny))
#     return res_max + matrix[x][y]
#
#
# def dfsmin(x, y):
#     if x == n - 1:
#         return matrix[x][y]
#     res_min = 100001
#     nd = d[y]
#     for i in range(len(nd)):
#         nx = x + nd[i][0]
#         ny = y + nd[i][1]
#         res_min = min(res_min, dfsmin(nx, ny))
#     return res_min + matrix[x][y]
#
# s_max, s_min = -1, 100001
# for i in range(3):
#     tmp_max = dfsmax(0, i)
#     tmp_min = dfsmin(0,i)
#     if s_max < tmp_max:
#         s_max = tmp_max
#     if s_min == -1:
#         s_min = tmp_min
#     else:
#         if s_min > tmp_min:
#             s_min = tmp_min
# print(s_max,s_min)


# 참고
# - 슬라이딩 윈도우 방식을 참고한다.
# - 배열방을 다 만들어놓고 내려가는 방식이 아니라.
# - 필요한 부분만 투 포인터로 옮겨가는 방식으로....

import sys
input = sys.stdin.readline

tmax = [0, 0, 0]
tmin = [0, 0, 0]
a = [0, 0, 0]
b = [0, 0, 0]
for i in range(int(input())):
    c = list(map(int, input().split()))
    tmax[0] = max(a[0], a[1]) + c[0]
    tmax[1] = max(a[0], a[1], a[2]) + c[1]
    tmax[2] = max(a[1], a[2]) + c[2]
    tmin[0] = min(b[0], b[1]) + c[0]
    tmin[1] = min(b[0], b[1], b[2]) + c[1]
    tmin[2] = min(b[1], b[2]) + c[2]
    a = tmax[:]
    b = tmin[:]
print(max(tmax), min(tmin))

# 다시풀기
# import sys
# input = sys.stdin.readline
# n = int(input())
#
# res_max = [0,0,0]
# res_min = [0,0,0]
# prev_max = [0,0,0]
# prev_min = [0,0,0]
#
# for i in range(n):
#     new = list(map(int,input().split()))
#     res_max[0] = max(prev_max[0],prev_max[1]) + new[0]
#     res_max[1] = max(prev_max[0],prev_max[1],prev_max[2]) + new[1]
#     res_max[2] = max(prev_max[1],prev_max[2]) + new[2]
#     res_min[0] = min(prev_min[0],prev_min[1]) + new[0]
#     res_min[1] = min(prev_min[0],prev_min[1],prev_min[2]) + new[1]
#     res_min[2] = min(prev_min[1],prev_min[2]) + new[2]
#     prev_max = res_max[:] # deep copy
#     prev_min = res_min[:]
#
# print(max(res_max),min(res_min))