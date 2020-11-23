# 백준 1541 | 잃어버린 괄호
## 문제
![image](https://user-images.githubusercontent.com/62331803/95876016-98dc2680-0dad-11eb-900d-b416c36338b5.png)

## 입력
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다.

## 출력
첫째 줄에 정답을 출력한다.

## 입출력 예제
![image](https://user-images.githubusercontent.com/62331803/95876107-b0b3aa80-0dad-11eb-8a0c-e6c312f1f5a9.png)

# 풀이
## 1차 (알고리즘 제대로 생각 못함) 
- '-'가 오면 묶고 다음 -에서 감싸줌

```python
import sys
expression = sys.stdin.readline().rstrip()
minus = []
for idx, w in enumerate(expression):
    if w == '-':
        minus.append(idx)

print(minus)

for i in range(len(minus)):
    expression = expression[:minus[i]+1] + '(' + expression[minus[i]+1:]
    for j in range(i+1,len(minus)):
        minus[j] += 1

if len(minus) % 2 == 1:
    expression += ')'

print(expression)
# 모르겟따
```

## 2차 (알고리즘 참고) ==> 성공
- '-'를 기준으로 나눈 뒤에
- 나눠진 배열방 값 연산하여 결과값에 다시 마이너스 연산

```python
import sys
expression = sys.stdin.readline().split('-')
results = []

for w in expression:
    res = 0
    nums = w.split('+')
    for n in nums:
        res += int(n)
    results.append(res)

ans = results[0]
for i in range(1,len(results)):
    ans -= results[i]
print(ans)
```

# 피드백
- '-'기준으로 나누고 나머지 배열방 계산해서 연산하기