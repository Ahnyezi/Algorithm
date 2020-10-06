import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
d = [0]*31
def dp(x):
    if x == 0: return 1 # 점화식을 위해 필요
    if x == 1: return 0 # 1인경우는 경우의수 존재 x
    if x == 2: return 3
    if d[x] != 0: return d[x]
    res = 3 * dp(x-2)
    for i in range(3,x+1):
        if i % 2 == 0:
            res += 2 * dp(x - i)
    d[x] = res
    return d[x]

print(dp(int(input())))