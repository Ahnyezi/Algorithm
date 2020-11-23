# 백준 11053 | 가장 긴 증가하는 부분 수열

![image](https://user-images.githubusercontent.com/62331803/96019303-50913700-0e87-11eb-83b0-6f024c19555f.png)


## 문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

## 입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다. 

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

## 출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

## 입출력 예제

![image](https://user-images.githubusercontent.com/62331803/96019374-69015180-0e87-11eb-994f-eba5262a24ea.png)

# 풀이
## 1차시도 (예제 맞았는데 오답)
- 매 시행마다 조건에 맞으면 prev에 넣어두고
- prev보다 현재 배열방 값이 크면 dp값 증가
```python
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))

dp = [0]*1000
dp[0] = 1
for i in range(1, N):
    prev = 0
    for j in range(i+1):
        if prev < A[j]:
            dp[i] += 1
            prev = A[j]
print(dp[N-1])
```

## 2차(반례 참고)==> 반례만 맞고 예제 틀림
- 4
- 1 4 2 3
- 해당 idx의 수보다 적은 수를 가진 항이 몇개인지 dp에 저장
```python
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))

dp = [1]*1000
for i in range(1, N): # i: DP 삽입 idx
    for j in range(i):
        if A[i] > A[j]: # 현재항보다 작은수를 가진 경우
            dp[i] += 1
print(dp[N-1])
```

## 3차 (3중 for문 ==> 시간초과)
- 현재방 이전의 배열들을 방문
- 포함/미포함 수인지 검사하여 현재 dp 방에 +1
```python
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))

dp = [1]*1000
for i in range(1, N): # i: DP 삽입 idx
    for j in range(i): # j: 현재 배열방 이전의 배열들 확인
        if A[i] > A[j]: # 현재항보다 작은수를 가진 경우
            flag = True
            for k in range(j): # 이미 포함된 수인지 검사
                if A[k] == A[j]:
                    flag = False
            if flag: # 이전에 없는 수일 경우에만 더해줌
                dp[i] += 1
print(dp[N-1])
```

## 4차 (알고리즘 참고) ==> 성공
- 자기자신보다 작은 숫자들 중 가장 큰 길이를 구하고
- 그 길이에 +1을 한다
```python
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
dp = [0] * N
for i in range(N):
    for j in range(i):# 0~i-1
        # 1) 현재항보다 작은 수
        # 2) 최대의 DP 값 가진 배열방
        if A[j] < A[i] and dp[j] > dp[i]: 
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
```

# 피드백
> print(max(dp))로 출력해야 함 *print(dp[N-1]) 불가
- 반례 : 1, 2, 3, 1, 2
- `print(max(dp)) # 3 (정답)`
- `print(dp[N-1]) # 2 (오답)`
- 이유: 전 항의 값 + 현재 항의 추가값 형태가 아니라, 길이마다의 최대값을 저장한 형태이기 때문