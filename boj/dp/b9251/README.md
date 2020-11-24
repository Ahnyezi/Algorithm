# 백준 9251 | LCS
<br>

[문제링크](https://www.acmicpc.net/problem/9251) <br>

:bulb: **풀이 | 다이나믹 프로그래밍**<br>
1. 핵심 아이디어
** 현재 인덱스에서 문자열 A의 문자와 문자열 B의 문자가 일치하는 경우**<br>

- (i,j)에서 A의 i번째 문자와 B의 j번째 문자가 같다면 최대문자열의 길이를 늘려줘야 한다
   - `if A[i-1] == B[j-1]:`
- A의 i-1번째와 B의 j-1번째 문자까지 비교했을 때 최대문자열의 길이에 +1을 한 값을 A의 i번째와 B의 j번째 문자까지 비교했을때 최대문자열 길이로 초기화 한다.
   - `dp[i][j] = dp[i-1][j-1] + 1`
<br>

** 문자열 A의 문자와 문자열 B의 문자가 일치하지 않는 경우**<br>
- 최대문자열 길이를 늘릴 수 없다. 
- 따라서, 현재 인덱스를 기준으로, 이전에 계산된 최대문자열의 길이 중 가장 큰 값을 가져온다
   - `dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])`
<br>


2. 주의할 점
- 두 문자열의 길이가 다를 수 있으므로, for문의 인덱스에 주의한다. 
- 비교하는 두 문자가 같을 경우, `dp[i-1][j-1]`의 값에 +1을 해줘야 한다. 

<br>

> 코드

```python
import sys
A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1 # 주의
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

for i in range(len(dp)):
    print(dp[i])

print(dp[len(A)][len(B)])
```
