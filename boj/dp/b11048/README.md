# 백준 11048 | 이동하기

[문제 링크](https://www.acmicpc.net/problem/11048)

<br>

:bulb: 풀이
- 핵심은 점화식 세우기
   - `(n+1,m+1)`: 점화식 사용을 위해서, 세로와 가로에 1칸씩 추가 
   - 인덱스가 i,j라고 할 때, i,j번째 방의 값은 `maze[i][j](현재 방의 사탕개수)` + `가능한 이전 시행의 값들 중 가장 큰 값`
      - `가능한 이전 시행의 값` : (i-1,j), (i,j-1), (i-1,j-1)
      - 따라서, `dp[i][j] = maze[i][j] + max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])`


<br>

> 코드

```python
import sys, time
input = sys.stdin.readline
n,m = map(int,input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input().split())))
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = maze[i][j] + max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
print(dp[n][m])
```