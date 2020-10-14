# 백준 2293 | 동전 1 (어려워.. 복습)

![image](https://user-images.githubusercontent.com/62331803/96020194-9b5f7e80-0e88-11eb-80df-560c1fa4fa09.png)

## 문제
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

## 입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다.

## 출력
첫째 줄에 경우의 수를 출력한다. 경우의 수는 2^31보다 작다.

## 입출력 예제
![image](https://user-images.githubusercontent.com/62331803/96020268-b92ce380-0e88-11eb-9c5c-3a1a8f5acecc.png)

# 풀이
## 1차 (못풀겠따)
- coins = [] 에 동전 배치
- k개수를 n개만큼 배치할 수 있는 모든 경우의 수 nCk
```python
import sys
input = sys.stdin.readline
n, k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

k % coins[0]

```

## 2차 (알고리즘 참고) ==> 알고리즘 이해자체가 어려웠음
#### dp 핵심은 어떻게 작은 문제로 나누거나 일반화 시킬 것이냐
> 핵심원리
1. 모든 동전 배열 coins에 담기
2. 동전 하나씩 빼서 해당 동전으로 k원을 만들 수 있는 경우의 수 dp[k]에 삽입
- coins = [1,2,5]
- dp = [0]*10001 # dp[k]: 1원 2원 5원으로 k값 만드는 경우의 수
- 1단계 : coins[0](1원)을 사용한 k값 만드는 경우의 수
    - dp[1] = 1, dp[2] = 1 ...... dp[k] = 1 (1원으로 k값 만드는 수 모든 경우 1가지)
- 2단계 : 만들어진 dp배열에 coins[1](2원)을 사용한 경우의 수 추가
    - dp[2] = dp[0](현재 동전의 가치뺀 가치를 만드는 경우의 수) + 1 (1단계에서 산출한 dp[2]값)
    - dp[3] = dp[1] + 1(1단계에서 산출한 dp[3]값), dp[4] = dp[2] + 1(1단계에서 산출해놓은 dp[4]값)
3. 모든 동전에 대한 경우의 수 구할 때까지 반복

> 세부동작원리
1. coins배열을 순회하는 인덱스의 값을 i라고 놓음 (동전을 하나씩 뽑기) ==> for i in range(len(coins)):
2. dp배열을 순회하는 인덱스 값을 j라고 놓았을 때,
   j의 범위를 현재 동전의 가치(coins[i])부터 목표 값(k)까지로 설정 ==> for j in range(c,k+1)
3. 이중 for문 돌면서, dp방에 새로운 동전을 사용해 만든 경우의 수 추가 ==> dp[j] += dp[j-i]
- j-i: 현재 동전의 가치를 뺀 가치의 경우의수가 담긴 dp방 idx


```python
import sys
n, k = list(map(int, sys.stdin.readline().split()))
coins = []
for _ in range(n):
    coins.append(int(input()))
dp = [0 for i in range(10001)]
dp[0] = 1
for i in coins:
    for j in range(i,k+1):
        dp[j] += dp[j-i]

print(dp[k])
```

# 피드백
- 알고리즘 쓰면서 이해하기
- coins 배열의 모든 값에 대하여, 현재 동전으로 k원을 만들 수 있는 경우의 수를 dp[k]에 저장
- coins의 모든 동전을 순회하면서 dp[k]값을 더해나감
- dp[k] = dp[k](기존의 동전을 사용하여 구한 경우의 수) + dp[k-c](현재 동전의 가치를 뺀 가치를 구하는 경우의 수)

### 참고
https://marades.tistory.com/5

https://pacific-ocean.tistory.com/200

https://mong9data.tistory.com/68
