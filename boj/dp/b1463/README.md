# 1463번 | 1로 만들기

## 문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다. 
<br>
- X가 3으로 나누어 떨어지면, 3으로 나눈다.
- X가 2로 나누어 떨어지면, 2로 나눈다.
- 1을 뺀다.
<br>
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
<br>

## 입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.
## 출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
<br>
![image](https://user-images.githubusercontent.com/62331803/95215793-586c2e00-082c-11eb-8cc1-c3eb89835f0c.png)
<br>
## 힌트
10의 경우에 10 -> 9 -> 3 -> 1 로 3번 만에 만들 수 있다.

# 의사코드
## 1차
- 큰 수로 나눌수록 횟수가 줄어들 것이라고 가정
- 무조건 3의 배수로 만드는 방식으로

```python

1차시도
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

while True:
    if x==1: break
    if x%3 == 0:
        x /= 3
    elif x%2 == 0 and (x/2)%3 == 0:
        x /= 2
    else:
        x -= 1
    cnt += 1
    print('cnt:'+str(cnt))
    print('x:'+str(x))

print(cnt)
```

### 결과
- 문제 이해 자체가 잘못됨
- 큰 수로 나누는 것이 능사가 아니다

## 2차시도
- 경우의 수를 모두 계산하여 최소값으로 배열을 초기화
- 점화식을 사용하자

```python
# 2차시도
import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n+1)

for i in range(2,n+1):
    # print('i:'+str(i))
    d[i] = d[i-1]+1
    if i%2==0: d[i] = min(d[i],d[i//2]+1)
    if i%3==0: d[i] = min(d[i],d[i//3]+1)
    # print(d[i])

print(d[n])
```

# 피드백
- 다이나믹 프로그래밍 언제 쓰는지 감잡기 ==> 많이 풀어보기!
- 무조건 큰 수로 나누는 것이 답이 아니다
- 모든 경우의 수 고려하는 경우도 생각하기 ==> 최소값을 정답으로 세팅
