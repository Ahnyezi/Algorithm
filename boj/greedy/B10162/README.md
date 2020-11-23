# 백준 10162 | 전자레인지
## 문제
![image](https://user-images.githubusercontent.com/62331803/95765899-708cf300-0ced-11eb-9569-aef698d2b87a.png)

## 입력
첫 번째 줄에는 요리시간 T(초)가 정수로 주어져 있으며 그 범위는 1 ≤ T ≤ 10,000 이다. 

## 출력
여러분은 T초를 위한 최소버튼 조작의 A B C 횟수를 첫 줄에 차례대로 출력해야 한다. 각각의 횟수 사이에는 빈 칸을 둔다. 해당 버튼을 누르지 않는 경우에는 숫자 0을 출력해야한다. 만일 제시된 3개의 버튼으로 T초를 맞출 수 없으면 음수 -1을 첫 줄에 출력해야 한다. 

## 입출력 예제
![image](https://user-images.githubusercontent.com/62331803/95765960-8995a400-0ced-11eb-92d4-eca4186558c0.png)

# 풀이 
## 1차 (예제 충족 x) 
- 조건식 잘못 줌
```python
import sys
input = sys.stdin.readline

btns = [60*5,60*1,10]
cnts = [0,0,0]

T = int(input())

flag = True
for _ in range(1000):
    for i in range(2,-1,-1):
        if T == 0:
            print(str(cnts[0])+' '+str(cnts[1])+' '+str(cnts[2]))
            flag = False
            break
        if T < 0:
            print(-1)
            flag = False
            break
        if btns[i] <= T:
            T -= btns[i]
            cnts[i] += 1
    if not flag:
        break
```

## 2차 (성공)
- 변경 전
```python
        if T < 0: # 안들어옴 
            print(-1)
            flag = False
            break
```
- 변경 후
```python
         if btns[2] > T: # 변경
            print('-1')
            flag = False
            break
```

```python
import sys
input = sys.stdin.readline

btns = [60*5,60*1,10]
cnts = [0,0,0]

T = int(input())

flag = True
for _ in range(1000):
    for i in range(3):
        if T == 0:
            print(str(cnts[0])+' '+str(cnts[1])+' '+str(cnts[2]))
            flag = False
            break
        if btns[2] > T:
            print('-1')
            flag = False
            break
        if btns[i] <= T:
            T -= btns[i]
            cnts[i] += 1
            break
    if not flag:
        break
```

## 다른 답안
- 10으로 나누어 떨어지는 경우와 아닌 경우로 분류
    - 버튼이 모두 10의 배수라는 성질 이용
- 한 번의 시행으로 완료
    - 나눗셈과 모드 연산 사용하여 한번에 처리

```python
import sys
input = sys.stdin.readline

T = int(input())
A,B,C = 0,0,0

if T % 10:
    print('-1')
else:
    A = int(T/300)
    T %= 300
    B = int(T/60)
    T %= 60
    C = int(T/10)
    T %= 10
    print(str(A)+' '+str(B)+' '+str(C))
```
