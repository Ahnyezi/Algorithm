# 백준 9466 | 텀 프로젝트

![image](https://user-images.githubusercontent.com/62331803/98676666-3cb1f580-239f-11eb-9ff9-f0baafe86248.png)
<br>

# 문제
![image](https://user-images.githubusercontent.com/62331803/98676716-4e939880-239f-11eb-9141-975ee1bcfa80.png)

## 입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫 줄에는 학생의 수가 정수 n (2 ≤ n ≤ 100,000)으로 주어진다. 각 테스트 케이스의 둘째 줄에는 선택된 학생들의 번호가 주어진다. (모든 학생들은 1부터 n까지 번호가 부여된다.)


## 출력
각 테스트 케이스마다 한 줄에 출력하고, 각 줄에는 프로젝트 팀에 속하지 못한 학생들의 수를 나타내면 된다.


## 입출력 예제
![image](https://user-images.githubusercontent.com/62331803/98676845-7c78dd00-239f-11eb-957d-04d6d062790a.png)


<br>

# 풀이
## 1차 (알고리즘 참고)  => 성공
- dfs
- 재귀 사용 X

```python
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    student = [0] + list(map(int,input().split()))
    visited = [0] * (n+1)

    group = 1
    for i in range(1,n+1):
        if visited[i] == 0:
            while visited[i] == 0:
                visited[i] = group
                i = student[i]
            while visited[i] == group:
                visited[i] = -1
                i = student[i]
            group += 1
    cnt = 0
    for v in visited:
        if v > 0: # -1과 0빼고 카운트
            cnt += 1
    sys.stdout.write("{}\n".format(cnt))
```

- 재귀 사용 O
```python
import sys
sys.setrecursionlimit(111111)

def dfs(x):
    global result
    visited[x] = True
    cycle.append(x) # 사이클을 이루는 팀을 확인
    number = numbers[x]

    if visited[number]: # 방문가능한 곳이 끝났는지 확인
        if number in cycle: # 사이클 가능 여부
            result += cycle[cycle.index(number)] # 사이클이 되는 구간 부터만 팀 이름
        return
    else:
        dfs(number)

for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int,input().split()))
    visited = [True] + [False] * N # 방문 여부
    result = []

    for i in range(1, N+1):
        if not visited[i]: # 방문 안한 곳이라면
            cycle = []
            dfs(i)

```