# 백준 2156 | 포도주 시식

## 문제

![image](https://user-images.githubusercontent.com/62331803/95647792-22b99480-0b0d-11eb-8cde-8ad115ff486b.png)

## 입력
첫째 줄에 포도주 잔의 개수 n이 주어진다. (1≤n≤10,000) 둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다. 포도주의 양은 1,000 이하의 음이 아닌 정수이다.

## 출력
첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.

## 입출력 예제

![image](https://user-images.githubusercontent.com/62331803/95647803-41b82680-0b0d-11eb-80ab-c58159376086.png)

# 풀이
## 1차 (33 아니라 32나옴)
- dp의 전 항을 고려안해줘서, 맨 마지막 번째 항이 최댓값이 아님
```python
import sys
input = sys.stdin.readline
N = int(input())
w = [0]
for i in range(N):
    w.append(int(input()))

# print(w)

dp = [0]*10001
dp[1]=w[1]
if N > 1:
    dp[2]=w[1]+w[2]

    for i in range(1,N+1):
        dp[i] = max(dp[i-3]+w[i-1],dp[i-2])+w[i]

print(dp)
print(dp[N])
```

## 2차(틀림)
- 오류: dp[i] = max(dp[i-3]+w[i-1],dp[i-2])+w[i]
```python
import sys
input = sys.stdin.readline
N = int(input())
w = [0]*10001
for i in range(1,N+1):
    w[i] = int(input())

dp = [0]*10001
dp[1]=w[1]
dp[2]=w[1]+w[2]
dp[3]=max(dp[1],dp[2])+w[3]

if N > 3:
    for i in range(4,N+1):
        dp[i] = max(dp[i-3]+w[i-1],dp[i-2])+w[i]

print(max(dp))
```

## 3차(반례 참고) => 성공
- 고치기 전: `dp[i] = max(dp[i-3]+w[i-1],dp[i-2])+w[i]` <br>
![image](https://user-images.githubusercontent.com/62331803/95647943-8e503180-0b0e-11eb-9abd-3b770ee45b0a.png) <br>

- 고친 후 : `dp[i] = max(dp[i-1],dp[i-3]+w[i-1]+w[i],dp[i-2]+w[i])`<br>
![image](https://user-images.githubusercontent.com/62331803/95647958-a9bb3c80-0b0e-11eb-9223-edea410c2bea.png) <br>

- 배열의 전 항도 고려해줘야 한다
    - 이유: dp[3] => 1000(dp[1])+1(w[3]), 0(w[0])+1000(w[2])+1(w[3]) < 2000(dp[2])
    - max 함수 안에 dp[2] 고려 안한다면 오답.
    - 그렇기 때문에, w[i]는 max 함수 안에다 각각 더해줘야 함.
    

```python
# 6
# 1000 1000 1 1 1000 1000
import sys
input = sys.stdin.readline
N = int(input())
w = [0]*10001
for i in range(1,N+1):
    w[i] = int(input())

dp = [0]*10001
dp[1]=w[1]
dp[2]=w[1]+w[2]
dp[3]=max(dp[2],w[1]+w[3],w[2]+w[3])

if N > 3:
    for i in range(4,N+1):
        dp[i] = max(dp[i-1],dp[i-3]+w[i-1]+w[i],dp[i-2]+w[i])

print(dp[N])
```

# 피드백
- 배열의 전 항 고려대상인지 아닌지 생각하기!

