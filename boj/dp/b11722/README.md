# 백준 11722 | 가장 긴 감소하는 부분 수열

![image](https://user-images.githubusercontent.com/62331803/99857630-f8a8c700-2bce-11eb-94b5-c2a4cd193a48.png)


## 문제
수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에 가장 긴 감소하는 부분 수열은 A = {10, 30, 10, 20, 20, 10}  이고, 길이는 3이다.


## 입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)


## 출력
첫째 줄에 수열 A의 가장 긴 감소하는 부분 수열의 길이를 출력한다.


## 입출력예제

![image](https://user-images.githubusercontent.com/62331803/99857678-1f66fd80-2bcf-11eb-8c5f-28f69f8727da.png)


# 풀이
## 1차시도 (시간초과)
- 갹 idx마다 idx +1부터 끝까지 순회
- nums[idx]보다 작은 nums 방의 가장 큰 값을 붙인 수열 생성
- `결과적으로 3중 for문 만들어진다 => 시간초과`

```python
import sys
input = sys.stdin.readline
N = int(input())
sequence = list(map(int,input().split()))
dp = [0]*N

for i in range(N):
    s = [sequence[i]]
    for _ in range(N-i): # 3) 1,2번을 남은 칸 수만큼 시행
        max_value = 0
        for j in range(i+1,N): # 1) 현재 값보다 작은 값 중 가장 큰 값 구함
            if sequence[j] < s[-1]:
               if sequence[j] > max_value:
                   max_value = sequence[j]
        if max_value != 0:
            s.append(max_value) # 2) 존재한다면, s에 삽입
    dp[i] = len(s)

print(max(dp))
```

## 2차시도(알고리즘 참고) 성공
- 각 idx마다 0부터 idx-1까지 순회
- 임시 리스트 s를 생성
- sequence[idx]보다 큰 sequence[j]를 만날 경우, dp[j]값을 s에 삽입
- s 초기화가 완료되면, s의 최댓값(기준 값보다 더 큰 수들의 수열길이 중 가장 큰 값)을 dp[idx]에 더하기

```python
import sys
input = sys.stdin.readline
N = int(input())
sequence = list(map(int,input().split()))
dp = [1 for i in range(N)]

for i in range(1,N): # i번째 자리에서 비교
    s = []
    for j in range(i):
        if sequence[i] < sequence[j]: # i 이전의 값들 중 sequence[i]보다 큰 수 sequence[j]를 찾으면
            s.append(dp[j]) # dp j번째 항을 s에 삽입 [j번째 값의 수열길이]
    if not s:
        continue
    else:
        dp[i] += max(s)
print(max(dp))
```