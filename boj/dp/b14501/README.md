# 백준 14501 | 퇴사


[문제링크](https://www.acmicpc.net/problem/14501)


:bulb: **풀이1 | 브루트 포스** <br>
[참고 블로그](https://suri78.tistory.com/178) <br>

- 퇴사날짜: `N`, 소요일수 리스트: `t`, 이익 리스트:`p`, 최대요금 리스트: `charge`

1. 우선 `charge`를 `p`배열값으로 초기화 한다. 
- `charge`는 i일차의 상담을 한다고 가정할 때의 최대요금을 저장하는 리스트
- 따라서, i일차의 상담을 한다고 하면 반드시 `Pi`는 `charge[i]`에 포함된다. 

2. 1일차부터 N일차까지 t와 p배열을 순회하며 모든 경우의 수를 체크

<img src="https://user-images.githubusercontent.com/62331803/100053429-62d99a00-2e63-11eb-9736-9a02f7d7f524.png" width="60%"> 
<br>

- i일차의 상담을 한다면, 다음에 상담가능한 날짜는 `i+Ti`일부터 `N`일까지이다.
   - N이 7이고 i가 1이라면(1일차의 상담을 한다면), 다음에 상담가능한 날짜는 1+T1인 `4`일부터 `7`일까지이다.
- `i`일차 상담을 한 이후에 `i+Ti`일차 상담을 한다면, `P[i] + P[i+Ti]` 라는 금액을 벌 수 있다. 
   - `1`일차 상담을 한 이후에 `4`일차 상담을 한다면, `10 + 20`이라는 금액을 벌 수 있다. 
   -  따라서 charge[4]에 `30`을 저장
- i값을 1부터 N까지 순회해가며, charge[i]로 가능한 모든 경우를 계산한 뒤, 가장 큰 값으로 초기화 한다.
- 이 때, `i+Ti`가 퇴사일 N이후가 되면 상담이 불가능하므로, charge[i]를 0으로 초기화 한다. 

<br>

> 코드

```python
import sys,copy
input = sys.stdin.readline
N = int(input()) # 퇴사날짜
t = [0 for _ in range(N+1)] # 소요일수
p = [0 for _ in range(N+1)] # 이익
for i in range(1,N+1):
    t[i],p[i] = map(int,input().split())
charge = copy.deepcopy(p) # 최대 요금 : 각 날짜의 상담을 할 경우 얻을 수 있는 금액으로 초기화

for i in range(1,N+1):
    if i + t[i] > N + 1: # 더이상 이동 불가능한 경우(퇴사일 이후)
        charge[i] = 0
    else:# 이동 가능한 경우
        for j in range(i+t[i],N+1): # 가능한 모든 경우를 다 따져본다
            new_charge = charge[i] + p[j]
            if new_charge > charge[j]:
                charge[j] = new_charge

print(max(charge))
```

<br>

:bulb: **풀이2 | 다이나믹 프로그래밍** <br>
[참고블로그](https://pacific-ocean.tistory.com/199) <br>

1. N일부터 1일까지 거꾸로 순회하며 dp리스트를 만든다.
- 퇴사 이전에 상담이 가능한 날짜 `i`를 만나면, 이전 시행의 최댓값 `dp[i+1]`과 `p[i]+dp[i+T[i]]`값을 비교하여 최댓값으로 charge[i]를 초기화 한다. 

>코드

```python
import sys,copy

input = sys.stdin.readline
N = int(input()) # 퇴사날짜
t = [0 for _ in range(N)] # 소요일수
p = [0 for _ in range(N)] # 이익
for i in range(N):
    t[i],p[i] = map(int,input().split())
dp = copy.deepcopy(p) + [0]

for i in range(N-1,-1,-1):
    if i + t[i] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1],p[i] + dp[i + t[i]])

print(dp[0])
```