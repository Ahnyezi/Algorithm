# 2579 | 계단오르기
## 문제

![image](https://user-images.githubusercontent.com/62331803/95402814-9744d580-094b-11eb-929e-8223ff215a43.png)
<br>

![image](https://user-images.githubusercontent.com/62331803/95402827-a166d400-094b-11eb-83c2-02fe218192ce.png)

<br>
![image](https://user-images.githubusercontent.com/62331803/95402839-a7f54b80-094b-11eb-9e44-1da0e1f358f6.png)

## 입력
입력의 첫째 줄에 계단의 개수가 주어진다.
<br>
둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.

## 출력
첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.

## 예제

![image](https://user-images.githubusercontent.com/62331803/95402896-ceb38200-094b-11eb-8994-8ca00753c096.png)

<br>

# 의사코드
## 1차 (알고리즘 자체를 생각 못함) 

- 규칙
   - 계단은 한번에 1칸 혹은 2칸 오를 수 있음 d[n] = d[n-1] + d[n-2]
   - 연속된 세 계단을 모두 밟을 수 없다.
   - 시작점은 계단에 포함되지 않는다
   - 마지막 도착 계단은 반드시 밟아야 한다. (도착점은 계단에 포함)
   - 계단의 개수는 300이하의 자연수

- 예시 분석
   - 10 20 15 25 10 20
   - d[0]= 0
   - d[1] = 10 [1]
   - d[2] => [1,2] = 30 or [2] = 20
   - d[3] => d[1]에서 2칸 or d[2]에서 1칸
   - [1,2,3](x) [1,3] = 25 or [2,3] = 35
   - d[4] = d[2]에서 2칸 or d[3]에서 1칸
   - d[2]에서 올라온 경우

- 다른 의사코드로
   - 1,2,4,6
   - 일단, 1칸2칸 올라갈 수 있다는 규칙으로 점화식 세워서 구하기
   - 구한 값이 연속 3개 수 있을 경우 제외
   - 마지막 도착 계단 안밟은 경우 제외

```python
import sys
input = sys.stdin.readline
N = int(input())
points = [0]
for _ in range(N):
    points.append(int(input()))
used = []
d = [0]*(N+1)
d[1] = points[1]
for i in range(2,N+1):
    if d[i-1]< d[i-2]:
        d[i] = d[i-2] + points[i]
        u = i-2
    elif d[i-1]> d[i-2]:
        d[i] = d[i-1] + points[i]
        u = i - 1
    else:
        pass
    if len(used) == 3:
        used.pop(0)
    used.append(u)
```

# 2차(알고리즘 참고. 런타임에러)
- 조건이 있는 경우에도 점화식을 세우는 데에 집중하기
    - 1) 연속하는 3 수 조건 없을 경우 점화식
    - d(n) = max(d(n-1) + points[n], d(n-2)+points[n])
    - 2) 연속하는 3 수 조건 적용할 경우 점화식 ==> 모든 조건 cover 가능
    - d(n) = max(d(n-3) + points[n-1] + points[n], d(n-2)+points[n])

```python
import sys
input = sys.stdin.readline
N = int(input())
points = [0] * (N+1)
for i in range(1,N+1):
    points[i] = int(input())

d = [0]*(N+1)
d[1] = points[1]
d[2] = max(d[1]+points[2],points[2])

for i in range(3,N+1):
    d[i] = max(d[i-3]+points[i-1]+points[i],d[i-2]+points[i])

print(d[N])
```

# 3차
- 런타임에러는 N=1일 때 COVER해주지 못하기 때문에 일어나는 문제였다.

- 배열방 최대값인 301로 만들기
```python
import sys
input = sys.stdin.readline
N = int(input())
points = [0] * 301 ##
for i in range(1,N+1):
    points[i] = int(input())

d = [0]*301 ##
d[1] = points[1]
d[2] = max(d[1]+points[2],points[2])

for i in range(3,N+1):
    d[i] = max(d[i-3]+points[i-1]+points[i],d[i-2]+points[i])

print(d[N])
```

- N == 1인 경우 잡아주기
```python
import sys
input = sys.stdin.readline
N = int(input())
points = [0] * (N+1)
for i in range(1,N+1):
    points[i] = int(input())

d = [0]*(N+1)
d[1] = points[1]

if N > 1:
    d[2] = max(d[1]+points[2],points[2])

    for i in range(3,N+1):
        d[i] = max(d[i-3]+points[i-1]+points[i],d[i-2]+points[i])

print(d[N])

```

- 배열방 N+2개로 만들기
```python
import sys
input = sys.stdin.readline
N = int(input())
points = [0] * (N+2)
for i in range(1,N+1):
    points[i] = int(input())

d = [0]*(N+2)
d[1] = points[1]
d[2] = max(d[1]+points[2],points[2])

for i in range(3,N+1):
    d[i] = max(d[i-3]+points[i-1]+points[i],d[i-2]+points[i])

print(d[N])

```

## 피드백
- 추가적인 조건 만족시킬 수 있는 점화식 세우는 것 중요
    - 연속된 세수 불가능하게 하는 점화식
- N이 1일 때 주의하기!!!
    - 기본 점화식에 사용되는 배열방 자체가 만들어지지 않으면, 런타임 에러 난다.
