# 백준 1965 | 상자넣기

<br>

[문제링크](https://www.acmicpc.net/problem/1965)

<br>

:bulb: **풀이** <br>
주어진 리스트에서 **가장 긴 오름차순 수열**을 찾는 문제와 동일하다.<br>

<br>

> 코드

```python
import sys
input = sys.stdin.readline

n = int(input())
box = list(map(int,input().split()))
dp = [1 for _ in range(n)] # 조건에 안 맞더라도 최소 1개 존재

for i in range(1,n):
    for j in range(i):
        if box[i] > box[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1

print(max(dp))
```
