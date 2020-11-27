# 상자넣기
import sys
input = sys.stdin.readline

n = int(input())
box = list(map(int,input().split()))
dp = [1 for _ in range(n)] # 조건에 안맞더라도 최소 1개는 있기 때문에

for i in range(1,n):
    for j in range(i):
        if box[i] > box[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1

print(dp)
print(max(dp))