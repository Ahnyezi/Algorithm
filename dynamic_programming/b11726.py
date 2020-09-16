# 점화식 구하는 방법
# a1,a2,a3..을 직접 그려보자
# if a1개수 + a2개수 = a3개수라면
# an = i*an-1 + j*an-2가 성립할 것
# a1과 a2의 고유한 개수를 세어 점화식에 대입하자.
# 예시) 전시행, 전전시행, 전전전시행을 고려하면서 점화식짜기 an = an-1 + an-2
# 첫째줄에 N 주어짐

# 파이썬의 재귀 깊이 한계치가 작아서 오류가 발생

import sys

sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
d = [0 for i in range(1001)]

def dp(x):
    if x==1: return 1
    elif x==2: return 2
    elif d[x]!=0: return d[x]
    d[x] = dp(x - 1) + dp(x - 2)
    return d[x] % 10007

print(dp(n))



