# 백준 1520 | 내리막 길 
<br>

[문제링크](https://www.acmicpc.net/problem/1520)
<br>

:bulb: **풀이**<br>

가능한 모든 경우의 수를 세어 반환하는 문제이다. <br>
dfs를 사용하여 맨 끝방에 도달한 경우만 `1`을 리턴하게 한 다음.<br>
호출한 곳으로 다시 돌아와 몇 개의 `1`이 리턴됬는지를 카운트한다. <br>

<br>

> **예제풀이 시각화** <br>

<img src="https://user-images.githubusercontent.com/62331803/100415781-4b4b1d00-30c0-11eb-84b6-b40fa2fa14e0.png" width="30%">
<br>


> **코드** <br>

```python
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
m,n = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)] # 방문 체크와 카운트를 함께 하기 위해 -1로 초기화

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and matrix[x][y] > matrix[nx][ny]:
            dp[x][y] += dfs(nx,ny)
    return dp[x][y]

print(dfs(0,0))
```
