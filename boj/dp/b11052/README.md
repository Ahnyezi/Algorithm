# 백준 11052 | 카드 구매하기

https://www.acmicpc.net/problem/11052

- 모든 경우의 수를 비교해 최댓값을 도출하기 때문에 다이나믹 프로그래밍을 사용한다
- 생각의 전환이 필요 ==> 다시 풀어보기

# 풀이

## 1차시도
- 의사코드
    - 나머지 존재하는 경우와 존재하지 않는 경우로 나눔
    - 존재하는 경우는, 나머지를 인덱스로 한 배열방 값을 더하여 최댓값을 만든다
- 문제점
    - 모든 경우 고려 안함
       - 예를 들어 N이 10이라면, (1,9) (2,8) (3,7)....로 경우를 나눔
       - 실제로는 (1,1,1,1,6), (2,2,6), (4,6) 등 훨씬 많은 경우가 존재한다.
- 반례
```python
# 10
# 1 100 160 1 1 1 1 1 1 1
# answer : 520 (2,2,3,3) 
# mine : 500 (2,2,2,2,2)
```

```python
import sys
input = sys.stdin.readline
N = int(input())
packs = [0] + list(map(int,input().split()))
dp = [0 for _ in range(len(packs))]

for i in range(1,len(packs)):
    remainder = N % i
    if remainder == 0: # 나머지 없음
        dp[i] = packs[i] * (N // i)
    else: # 나머지 있음
        for j in range(len(packs)):
            if remainder == j:
                dp[i] = packs[i] * (N // i) + packs[j]

print(max(dp))
```

## 정답
- DP개념 사용하여, 인덱스가 1번인 방부터 하나씩 채워나가기
- 모든 경우의 수를 고려한다.
    - dp[i] => i개의 카드를 구매할 때의 최대가격
    - 만약 i + j = N이 된다면, (i,j)의 형태로 모든 경우의 수를 표현할 수 있다.
    - 예를 들어, dp[4]를 구하려 한다면, dp[1] + price[3] 와 dp[2] + price[2]와 dp[3] + price[1]을 비교해야 한다. 
    - 일반항: `if dp[i] < dp[i-j] + price[j] : dp[i] = dp[i-j] + price[j]`

```python
import sys
input = sys.stdin.readline
N = int(input())
price = [0] + list(map(int,input().split()))
dp = [0]*(N + 1)
dp[1] = price[1]

for i in range(2,N+1):
    for j in range(1,i+1):
        if dp[i] < dp[i-j] + price[j]:
            dp[i] = dp[i-j] + price[j]

print(dp[N])

```