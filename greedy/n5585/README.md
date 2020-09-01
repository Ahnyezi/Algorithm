(9/1 화)

# 문제5585 | 거스름돈 ☆

## 피드백

### 1. 뺄셈말고 나눗셈도 가능 <br/>

## 문제
<details>
<summary> 문제보기 </summary>

타로는 자주 JOI잡화점에서 물건을 산다. JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 언제나 거스름돈 개수가 가장 적게 잔돈을 준다. 타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.

예를 들어 입력된 예1의 경우에는 아래 그림에서 처럼 4개를 출력해야 한다.<br/>
<img src="https://user-images.githubusercontent.com/62331803/91864162-dd52ad80-ecaa-11ea-8ebc-e5b98960cf1f.png" width="50%">

<br/>

#### 입력
입력은 한줄로 이루어져있고, 타로가 지불할 돈(1 이상 1000미만의 정수) 1개가 쓰여져있다.

#### 출력
제출할 출력 파일은 1행으로만 되어 있다. 잔돈에 포함된 매수를 출력하시오.

#### 입출력예시 <br/> 
<img src="https://user-images.githubusercontent.com/62331803/91864329-0c691f00-ecab-11ea-8994-5f3001c6a1e0.png" width="50%">

</details>

<br/>


## 전체코드

#### 내풀이

```python
import sys

if __name__ == "__main__":
    coins = [500,100,50,10,5,1]
    money = int(sys.stdin.readline())
    change = 1000 - money
    count = 0

    while True:
        if change <= 0:
            break
        for c in coins:
            if change >= c:
                change -= c
                count += 1
                break

    print(count)

'''
# 1차시도
import sys

if __name__ == "__main__":
    coins = [500,100,50,10,5,1]
    money = int(sys.stdin.readline())
    change = 1000 - money
    count = 0

    for c in coins:
        if change == 0:
            break
        if change >= c:
            change-=c
            count+=1

    print(count)
'''

#### 다른풀이

```python

import sys

change = 1000 - int(sys.stdin.readline())
coins = [500,100,50,10,5,1]
count = 0

for c in coins:
    count += change//c
    change %= c

print(count)


```

```
