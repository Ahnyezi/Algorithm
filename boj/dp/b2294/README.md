# 백준 2294 | 동전2

:bulb: **풀이**<br>
`n`개의 동전으로 `k`원을 만들 때, `k`원을 만들 수 있는 최소 동전의 개수를 return한다. <br>
동전의 개수만큼 반복문을 실행하며, **배열 idx가치를 만들 수 있는 최소 동전의 개수를 초기화 해 나간다**. <br>
<br>

점화식은 다음과 같이 세울 수 있다. <br>
`dp[j] = dp[i-coins[i]] + 1`<br>

`dp[j]`: `j` 가치를 만들 수 있는 최소 동전의 개수 <br>
`dp[j-coins[i]] + 1`: **현재 배열방의 가치 - 현재의 시행에서 사용 중인 동전의 가치**를 만들 수 있는 최소 동전의 개수 + 1
- (예) `j` : 6, `coins[i]` : 5이라면, 6이라는 가치를 만들기 위한 동전의 최소 개수는 dp[6-5]인 `dp[1]` + 1한 값과 같다. 
<br>

하지만 해당 **점화식은 일부 경우에 사용할 수 없다**. <br>
**주어진 동전을 모두 사용해도 만들 수 없는 가치가 있으며, 그러한 동전들을 배제해야 하기 때문**이다. <br>
그러한 경우를 처리하기 위해서, <br>
연산 전에 `dp`배열의 모든 방 값을 **k의 가용범위를 넘어서는 숫자인 `10001`로 초기화**한다.<br>
그 후에, 위에서 세운 점화식을 실행하기 위한 조건으로<br>
`if dp[j] > dp[j-coins[i]] + 1:`을 설정해 놓는다.<br>
<br>

이 말은 j라는 인덱스 배열방`j 가치를 만들기 위한 최소 동전의 개수`가<br>
현재의 동전으로 재연산 한 후의 값`dp[j-coins[i]]+1`보다 클 경우에만 실행되며,<br>
만일 `dp[j-coins[i]]`의 값이 10001 즉, 어떠한 동전으로도 만들 수 없는 가치라면<br>
해당 점화식을 사용할 수 없기 때문에 다음으로 넘어가게 된다. <br>
<br>

이 규칙을 사용하여 구현한 코드는 다음과 같다. <br>

> 코드

```python
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input().rstrip()))
dp = [10001 for _ in range(k+1)]
dp[0] = 0 # 점화식 사용을 위한 0번째 배열방 setting

for i in range(n):
    for j in range(coins[i],k+1):
        if dp[j] > dp[j-coins[i]] + 1:
            dp[j] = dp[j-coins[i]] + 1

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
```








