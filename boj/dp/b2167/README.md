# 백준 2167 | 2차원 배열의 합

https://www.acmicpc.net/problem/2167

1. dp를 사용하여 푼다. 
   - 주어진 배열과 동일한 크기의 2차원 dp를 생성
   - `dp[i][j]`에는 0,0부터 i,j까지 원소의 합을 담는다.
2. dp에 사용할 점화식 구하기
<img src="https://user-images.githubusercontent.com/62331803/99933919-c1d5db00-2d9f-11eb-9dc0-ba406ddb5dc5.jpg" width="40%">
<br>
   - dp[3][3]을 구한다고 생각해보자.
      - dp[3][3]은 (0,0)부터(3,3)까지의 배열 원소를 모두 더한 값이다. 
      - 그림에 나와있는 arr배열에서 보면 보라색 영역의 넓이를 구하는 것이다. 
   - 이 때
      - `보라색 영역의 넓이 = arr배열의 (3,3) 원소 + 노란색 영역의 넓이 + 파란색 영역의 넓이 - 초록색 영역의 넓이`로 나타낼 수 있다. 
      - 즉, `dp[3][3] : arr[3][3] + dp[3][2] + dp[2][3] - dp[2][2]`이다.
   - 따라서, `dp[i][j] = arr[i][j] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]` 라는 식을 도출해 낼 수 있다. 
3. 특정 영역 합 구하기
   - dp에 저장되어 있는 값은 0,0부터 i,j까지의 합이다.
   - 하지만, 실제 문제에서 요구하는 답은 i1,j1부터 i2,j2까지의 합이므로 이를 고려해서 식을 구하면
   - 구하고자하는 영역의 합은 주어진 영역이 `i1,j1,i2,j2`라고 두었을 때,
   -  `dp[i2][j2]-dp[i1-1][j2]-dp[i2][j1-1]+dp[i1-1][j1-1]`이다

<br>
# 풀이
```python
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [0 for _ in range(N+1)]
arr[0] = [0 for _ in range(M+1)]
for i in range(1,N+1):
    arr[i] = [0] + list(map(int,input().split()))

# 배열 arr의 0,0부터 i,j 번째까지 원소 합
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = arr[i][j] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

K = int(input())
for _ in range(K):
    i1,j1,i2,j2 = map(int,input().split())
    print(dp[i2][j2]-dp[i1-1][j2]-dp[i2][j1-1]+dp[i1-1][j1-1])
```