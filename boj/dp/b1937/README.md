# 백준 1937 | 욕심쟁이 판다
<br>

[문제링크](https://www.acmicpc.net/problem/1937)
<br>

:bulb: **풀이** <br>
- n*n크기의 이차원 행렬이 주어진다.
- 판다가 각 인덱스에 위치할 때, 살 수 있는 최대날짜를 출력해야 한다.
   - dfs를 통해서 각 인덱스에 위치할 때 갈 수 있는 경로를 방문한다.
   - 모든 경로를 방문하여 최대값을 dp에 저장한다.

<br>

> 코드

```python
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
		# 이전에 최대경로를 구했다면 dp에 -1이상의 값이 저장되어있으므로, 바로 return
    if dp[x][y] == -1: # 아직 최대경로를 구하지 않았다면, 현재 인덱스에서 파생되는 인덱스를 모두 확인하여 최댓값을 dp에 저장
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and forest[x][y] < forest[nx][ny]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny))
        dp[x][y] += 1
    return dp[x][y]

max_days = 0
for i in range(n):
    for j in range(n):
        max_days = max(max_days, dfs(i, j))
print(max_days)

```

<br>

<img src="https://user-images.githubusercontent.com/62331803/100318690-cb5e7d80-3001-11eb-8d57-5bc515cfcbd1.png" width="50%">










