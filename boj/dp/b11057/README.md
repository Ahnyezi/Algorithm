# 백준 11057 | 오르막 수

https://www.acmicpc.net/problem/11057

- 이해하기 매우 어려웠음
- 이차원 dp를 사용하는 문제
   - 1차원으로 계속 시도했다가 시간 초과났다. 
   - 주어지는 값인 N이 수의 길이라는 점과 최대 N이 1000이라는 점을 고려하면, 1차원 dp로 풀 수 없다는 것을 알 수 있다.
- 핵심 논리
   - 2차원 dp 생성 시, 모든 값에 해당하는 배열방을 만들지 않는다.
   - 외부 idx(수의 길이, 자릿수)는 0~1001까지 만든다. 
   - 내부 idx(끝자리 숫자)는 0~9까지 만든다. 
   - 즉, 각 자릿수에서 끝자리숫자가 공통되는 숫자의 개수를 담은 리스트를 생성한다. 
   - `dp[2][3] : 자릿수가 2인 숫자 중에 3으로 끝나는 숫자의 개수` => 4개 (03 13 23 33)
   - dp가 완성되면, i가 주어진 N값과 같을 때의 dp[N] 배열방의 값을 모두 더한다.
   - N이 3이라면, `sum(dp[3])%10007`이 답임. 즉, 자릿수가 3인 모든(끝자리가 0부터 9까지인) 숫자의 개수 합을 출력한다. 

# 정답
```python
import sys
N = int(sys.stdin.readline()) # 자릿수
dp = [[0]*10 for i in range(1001)] # 10 : 끝 자리가 0~9인 숫자의 개수, 1001: 최대 자릿수

for i in range(10): # 자릿수 1개일 때 배열방값 초기화
    dp[1][i] = 1

for i in range(2,1001):
    for j in range(10):
        for k in range(j+1):
            # dp[i][j]: 자릿수가 i이면서 끝자리가 j인 숫자의 개수는
            # dp[i-1][k] : 자릿수가 i-1이면서 끝자리가 j이하인 모든 숫자의 덧셈으로 구한다.
            dp[i][j] += dp[i-1][k] 
            
print(sum(dp[N])%10007)
```