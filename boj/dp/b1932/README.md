# 백준 1932 | 정수삼각형

## 문제 

![image](https://user-images.githubusercontent.com/62331803/95593760-0d008c80-0a85-11eb-83ac-c2553d8c3ee3.png)

## 입력
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

## 출력
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

## 입출력 예제

![image](https://user-images.githubusercontent.com/62331803/95593868-2b668800-0a85-11eb-8053-7960b2c82890.png)

# 풀이
## 1차시도 (모든 경우 고려하지 않고, 현 시점에서 가장 큰 경우만 따라감)

```python
import sys
input = sys.stdin.readline
N = int(input())
square = [0]
for i in range(1,N+1):
    s = input()
    if ' ' in s:
        ss = s.split(' ')
        ns = list(map(int,ss))
        square.append(ns)
    else:
        square.append(int(s))

d = [0,square[1]]
idx = 0
for i in range(2,N+1):
    if square[i][idx] <= square[i][idx+1]:
        d.append(d[i-1]+square[i][idx+1])
        idx += 1
    elif square[i][idx] > square[i][idx+1]:
        d.append(d[i-1]+square[i][idx])

print(d[-1]) # 28
```

## 2차시도(예제 다시 보기)
- DP를 2차원으로 생성하여 모든 경우를 고려하기
   - 각 자리에 올 수 있는 최대값을 저장하는 2차원 배열 DP
   - 각 라인의 끝자리에 있는 경우가 아니라면, 경우의 수 2가지
   - 중간에 있는 경우에만 MAX 함수로 최댓값을 넣어준다.

```python
import sys
input = sys.stdin.readline
N = int(input())
square = [0]
for i in range(1,N+1):
    s = input()
    if i == 1:
        square.append(int(s))
    else:
        ss = s.split(' ')
        ns = list(map(int,ss))
        square.append(ns)

# print(square)
dp = [0]*500

for i in range(1,N+1):
    for j in range(i):
        pass
```
> 그래도 모르겠다

## 3차시도(다른 답안 참고)
- square 자체를 2차원 dp 배열로 사용하기

```python
import sys
input = sys.stdin.readline
N = int(input())
dp = []
for i in range(N):
    dp.append(list(map(int,input().split())))

for i in range(1,N):
    for j in range(i+1):
        if i == 1:
            dp[1][j] += dp[0][0]
        else:
            if j == 0:
                dp[i][0] += dp[i-1][0]
            elif j == i:
                dp[i][i] += dp[i-1][i-1]
            else:
                dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])

max = dp[N - 1][0]
for i in range(1,N):
    if dp[N-1][i] > max:
        max = dp[N-1][i]

print(max)
```

# 피드백
- DP란 모든 경우를 고려하여, 배열방에 저장한 뒤 최적의 값을 구하는 방법
   - 즉, 모든 경우를 다 고려해야 함.
- 삼각형 문제 패턴 이해하기
   - 주어지는 값 자체를 2차원 DP배열로 사용
   - 인덱스가 끝일 경우 그냥 내려오고, 중간일 경우 max함수 사용