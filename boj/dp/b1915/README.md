# 백준 1915 | 가장 큰 정사각형

<br>

[문제링크](https://www.acmicpc.net/problem/1915)

<br>

:bulb: **풀이**<br>
bfs로 풀려고 했다가 정사각형이라는 조건을 확인하고 이중 for문을 활용하여 dp로 풀었다. <br>
`dp`의 각 방에는 현재 인덱스에서 가질 수 있는 **정사각형 최대 변의 길이**를 넣는다. <br>
만약 현재 있는 칸의 값이 `1`이고, 인덱스가 `i,j`라고 할 때, <br>
정사각형을 이룰 수 있는 `연관 인덱스(i,j-1/i-1,j-1/i-1,j)`들을 방문하여<br>
현재 위치에서 정사각형 최대변의 길이를 dp 방에 삽입한다.<br>
**정사각형**을 구성해야 하기 때문에, **연관 인덱스 3개 배열방의 최소값**<br>
즉, **3개의 배열방을 고려했을 때 만들 수 있는 최소 정사각형 한변의 길이**를 가져온 뒤에<br>
해당 값에 +1한 값을 dp의 현재 배열방에 넣어준다. <br>

<br>


> 코드

```python
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
matrix = [list(map(int,list(input().rstrip()))) for _ in range(n)]
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

length = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if matrix[i-1][j-1] == 1:
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
            if dp[i][j] > length:
                length = max(length, dp[i][j])

print(length**2)
```



