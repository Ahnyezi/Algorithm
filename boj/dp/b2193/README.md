# 2193번 | 이친수
## 문제
0과 1로만 이루어진 수를 이진수라 한다. 이러한 이진수 중 특별한 성질을 갖는 것들이 있는데, 이들을 이친수(pinary number)라 한다. 이친수는 다음의 성질을 만족한다.<br>
<br>
이친수는 0으로 시작하지 않는다.<br>
이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.<br>
예를 들면 1, 10, 100, 101, 1000, 1001 등이 이친수가 된다. 하지만 0010101이나 101101은 각각 1, 2번 규칙에 위배되므로 이친수가 아니다.<br>
<br>
N(1 ≤ N ≤ 90)이 주어졌을 때, N자리 이친수의 개수를 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 N이 주어진다.

## 출력
첫째 줄에 N자리 이친수의 개수를 출력한다.

## 입출력 예제
![image](https://user-images.githubusercontent.com/62331803/95593156-4be21280-0a84-11eb-9968-744f8c341ecb.png)

<br>

# 풀이
## 1차시도 
- 앞의 배열에서 +0, +1을 한 결과를 모든 배열에 넣고
- 각 항을 검사하여 조건에 맞는 것만 count

```python
import sys
input = sys.stdin.readline
N = int(input())

def check(s):
    print('test:'+s)
    if s[0] == '0':
        return False
    if '11' in s:
        return False
    return True

dp =[]
for i in range(1,N+1):
    dp.append([0]*i)

dp[0][0] = '1'
for i in range(1,N+1):
    print('i:'+str(i))
    for j in range(len(dp[i-1])):
        if check(str(dp[i-1][j])+'0'):
            print('성공:'+str(dp[i-1][j])+'0')
        elif check(str(dp[i-1][j])+'1'):
            print('성공:'+str(dp[i-1][j])+'1')

print(dp)
```

> 모르겟다..

## 2차시도 (답안 알고리즘 참고--> 점화식을 세워라)
- 각 시행을 직접 나열해서 규칙을 찾는다
- 모든 시행은 전시행 + 0, 전전시행 + 10이라는 규칙을 가짐
- 이것을 토대로 점화식을 세우면,
- dp[n] = dp[n-1]+dp[n-2]

```python
import sys
input = sys.stdin.readline
N = int(input())

dp = [0]*90
dp[0] = 1
dp[1] = 1

for i in range(2,N+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[N-1])
```
> 런타임 에러
N=90일 경우, dp배열에 90개의 방밖에 없기 때문에 index out of range 에러 뜸<br>

![image](https://user-images.githubusercontent.com/62331803/95593450-ada27c80-0a84-11eb-829a-e31a1c575313.png)


## 3차시도 (배열방 개수 91개로 늘리기) ==> 성공

```python
import sys
input = sys.stdin.readline
N = int(input())

dp = [0]*91
dp[0] = 1
dp[1] = 1

for i in range(2,N+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[N-1])
```

# 피드백
- 점화식 세우기의 중요성  ==> 나열해서 규칙 찾기
- 배열방 세팅 중요성 ==> N=1일  때, N=max num 일 때를 잘 고려
