# 백준 2294 | 동전2

:bulb: **풀이**<br>
- DP를 이용하여, 가능한 모든 경우를 구한다.
- 점화식이 핵심
   - 배열 `dp`는 10001로 초기화하여, 모든 경우에 점화식을 이용할 수 있는 조건문이 실행되도록 한다. 

```python
dp = [10001 for _ in range(k+1)] # k의 최댓값인 10000보다 큰 수로 초기화
.
.
.
        if dp[j] > dp[j-coins[i]] + 1: # 모든 경우에 해당 조건문이 실행되도록 한다. 
            dp[j] = dp[j-coins[i]] + 1
```

- `dp[j] = dp[j-coins[i]] + 1`: 전 시행에서 구해진 값 + 1
```python
# ex) dp[10] = dp[10-coins[1]] + 1
#            = dp[10- 5] + 1
#            = dp[5] + 1
#            = 1 + 1
```

<br>

> 코드

```python
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [10001 for _ in range(k+1)
dp[0] = 0 # 0원이 되는 경우는 없음

for i in range(n):
    for j in range(coins[i],k+1):
        if dp[j] > dp[j-coins[i]] + 1:
            dp[j] = dp[j-coins[i]] + 1 

if dp[k] == 10001: 
    print(-1)
else:
    print(dp[k])
```