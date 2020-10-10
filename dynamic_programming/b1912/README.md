# 백준 1912 | 연속합
## 문제
![image](https://user-images.githubusercontent.com/62331803/95647699-82637000-0b0c-11eb-9c3b-f332c29354a3.png)

## 입력
첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

## 출력
첫째 줄에 답을 출력한다.

## 입출력 예제
![image](https://user-images.githubusercontent.com/62331803/95647712-95764000-0b0c-11eb-8676-dde15c0f118f.png)
![image](https://user-images.githubusercontent.com/62331803/95647715-9d35e480-0b0c-11eb-9c0a-e6cc1643f8a7.png)

# 풀이
## 1차 (예제 충족 못시킴)
- 연속된 몇 개의 수를 선택해서 합이 가장 큰 합 구하기
```python
import sys
input = sys.stdin.readline
N = int(input())
seq = list(map(int,input().split()))

dp = [0] * 100001
dp[1] = seq[0]

if N > 1:
    for i in range(2,N+1):
        dp[i] = max(dp[i-1],seq[i-2]+seq[i-1],seq[i-1])

print(dp) # 예제 충족 못시킴
```

## 2차 (성공) 
```python
import sys
input = sys.stdin.readline
N = int(input())
seq = list(map(int,input().split()))

dp = [0] * 100001
dp[1] = seq[0]

if N > 1:
    for i in range(2,N+1):
        dp[i] = max(dp[i-1]+seq[i-1],seq[i-2]+seq[i-1],seq[i-1])

answer = max(dp)
if answer == 0:
    answer = dp[1]
    for i in range(1,N+1):
        if dp[i] == 0:
           answer = 0
           break
        else:
            if dp[i] > answer:
                answer = dp[i]

print(answer)
```

# 피드백
- 수열의 모든 항이 음수일 때 max값 0으로 나오는 것 주의