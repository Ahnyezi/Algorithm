# 1003 | 피보나치 함수

## 문제

![image](https://user-images.githubusercontent.com/62331803/95402567-040ba000-094b-11eb-9dec-e128d4b8954b.png)
<br>

## 입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.<br>
각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

## 출력
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

## 예제

![image](https://user-images.githubusercontent.com/62331803/95402630-2b626d00-094b-11eb-8221-1ce095e32ae6.png)

# 의사코드
```
재귀함수로 피보나치 수열 구할 경우,
fibonacci(3) ==> return fibo(2) + fibo(1)

fibo(2) ==> return fibo(1) + fibo(0)
fibo(1) ==> print('1'), return 1

fibo(1) ==> print('1'), return 1
fibo(0) ==> print('0'), return 0

즉, 1은 2번 호출되고, 0은 한번 호출됨.

fibo(4)일 경우
return fibo(3) + fibo(2)

fibo(3) ==> return fibo(2) + fibo(1)
fibo(2) ==> return fibo(1) + fibo(0)

fibo(2) ==> return fibo(1) + fibo(0)
fibo(1) ==> print('1'), return 1
fibo(1) ==> print('1'), return 1
fibo(0) ==> print('0'), return 0

fibo(1) ==> print('1'), return 1
fibo(0) ==> print('0'), return 0

즉, 1은 3번 호출되고, 0은 2번 호출됨.

fibo(5)일 경우
return fibo(4) + fibo(3)

fibo(0) 일 때, 1 0
fibo(1) 일 때, 0 1
fibo(2) 일 때, 1 1
fibo(3) 일 때, 1 2
fibo(4) 일 때, 2 3  즉, 바로 앞결과 + 앞앞 결과
```

# 1차시도 (성공)
```python
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    # d = [0]*(N+1)
    d = [(1,0),(0,1)]
    for i in range(2,N+1):
        d.append((d[i-1][0]+d[i-2][0],d[i-1][1]+d[i-2][1]))
    print(str(d[N][0])+" "+str(d[N][1]))
```