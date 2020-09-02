(9/2 수)

# 문제2217 | 로프 ☆

## 피드백

### 1. 항상 제한사항에 주의하자
- 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다


### 2. 다른풀이
- 리스트를 하나만 생성해두고
- temp 변수를 사용하여 최대값 즉시 변경

```python

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    arr = []

    for i in range(N):
        arr.append(int(input()))
    arr.sort(reverse=True)

    m = 0
    for i in range(len(arr)):
        temp_max = arr[i] * (i+1)
        if temp_max > m:
            m = temp_max

    print(m)


```

<br/>

## 문제
<details>
<summary> 문제보기 </summary>

N(1≤N≤100,000)개의 로프가 있다. 이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다. 각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.<br/> 
<br/> 
하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다. k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.<br/> 
<br/> 
각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오. 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.<br/> 
<br/> 

## 입력
첫째 줄에 정수 N이 주어진다. 다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다. 이 값은 10,000을 넘지 않는 자연수이다.
<br/> 

## 출력
첫째 줄에 답을 출력한다.
<br/> 

#### 입출력예시 <br/> 
<img src="https://user-images.githubusercontent.com/62331803/92003369-ea8b9d00-ed7b-11ea-928d-ac11ab01e450.png" width="50%">



</details>

<br/>


## 전체코드

#### 내풀이(2차시도에 성공)

```python
# 2차시도
# 제약조건: 모든 로프를 사용할 필요 없다. 임의로 몇 개만 골라 사용 가능
# 고려할 사항: 1개 사용하는 경우, 2개 사용하는 경우, .... n개 사용하는 경우 나눈 뒤에
# 최대값 가져오기

# 1개 사용하는 경우: sorting해서 가장 큰 거 1개
# 2개 사용하는 경우: sorting해서 가장 큰 2개 중 작은거 * 2
# 3개 사용하는 경우: sorting해서 가장 큰 3개 중 가장 작은거 * 3

import sys
rope = []
max = []

num = int(sys.stdin.readline())
for i in range(num):
    rope.append(int(sys.stdin.readline()))

rope = sorted(rope, reverse=True)

for i in range(num):
    max.append(rope[i] * (i+1))

print(sorted(max)[num-1])

```

#### 1차시도(실패) - 너무 단순하게 생각함
```python

# 1차시도
# import sys
# rope = []
# max = []
#
# num = int(sys.stdin.readline())
# for i in range(num):
#     rope.append(int(sys.stdin.readline()))
#
# rope = sorted(rope)
#
# print(rope[0]*num)
'''

