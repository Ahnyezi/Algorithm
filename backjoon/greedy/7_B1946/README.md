(9/3 목)

# 문제1946 | 신입사원 ☆☆

## 피드백

### 1. Case 여러개인 경우, 들여쓰기/초기화 위치 주의
- 오류 | 들여쓰기, 초기화

```python
if __name__ =="__main__":
    score = [] # 초기화: 모든 case에 대해 한번만 초기화 되고, 다음 case부터 뒤에 추가됨

    cases = int(sys.stdin.readline())
    for i in range(cases):
        num = int(sys.stdin.readline())
        for j in range(num):
            rm, iv = map(int, sys.stdin.readline().split(' '))
            score.append((rm,iv))
    
    print(newcomer(score)) # 들여쓰기: 모든 case에 대해 한번만 print 됨
```

- 수정
```python
if __name__ =="__main__":
    cases = int(sys.stdin.readline())
    for i in range(cases):
        # score 위치 조정
        score = []
        num = int(sys.stdin.readline())
        for j in range(num):
            rm, iv = map(int, sys.stdin.readline().split(' '))
            score.append((rm,iv))

        # print문 위치 조정
        print(newcomer(score))
```



- 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다

<br/>

### 2. 다른풀이
- sorted함수 없이, 직접 1차원 리스트를 생성해서 비교

```python

import sys

input = sys.stdin.readline

test = int(input())
for i in range(test):
    n = int(input())
    score = [0 for i in range(n+1)]
    for j in range(n):
        rm, iv = map(int, input().split())
        score[rm] = iv # 각 사람의 면접 순위를 서류심사 순으로 오름차순 정렬
                        # 가장 앞에 있는 사람이 1등 (무조건 합격)
    min = score[1]
    cnt = 0
    print('score:',score)
    for k in range(2, n+1):
        if score[k] > min:
            cnt += 1
        else:
            min = score[k]

    print(n-cnt)

```

<br/>

## 문제
<details>
<summary> 문제보기 </summary>

언제나 최고만을 지향하는 굴지의 대기업 진영 주식회사가 신규 사원 채용을 실시한다. 인재 선발 시험은 1차 서류심사와 2차 면접시험으로 이루어진다. 최고만을 지향한다는 기업의 이념에 따라 그들은 최고의 인재들만을 사원으로 선발하고 싶어 한다.<br/> 
<br/> 
그래서 진영 주식회사는, 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.<br/> 
<br/> 
이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램을 작성하시오.<br/> 
<br/> 

### 입력
첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다. 각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다. 두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다고 가정한다.<br/> 

### 출력
각 테스트 케이스에 대해서 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원수를 한 줄에 하나씩 출력한다.<br/> 


#### 입출력예시 <br/> 
<img src="https://user-images.githubusercontent.com/62331803/92065796-45081600-eddb-11ea-9e3d-ed8ff992aa4b.png" width="50%">



</details>

<br/>


## 풀이

#### 문제이해
다른 지원자들과 비교해서 서류심사, 면접시험 성적중<br/>
적어도 하나가 다른 지원자보다 떨어지지 않는자만 선발<br/>
예를 들어 A와 B를 비교했을 때,<br/>
A(7,3) B(4,2)라면 A[0]>B[0]이면서 A[1]>B[1]이기 때문에<br/>
B는 조건에 맞지 않는다.<br/>

#### 의사코드 (오답)
서류 심사로 정렬해서 ~~뒤에 사람 값과 비교~~ **서류는 이미 정렬된 상태이기 때문에, 면접 순위만 비교** <br/>
~~조건에 맞지 않으면,~~ people 수를 하나씩 줄여간다. **(조건) 현재 채용된 사람의 면접 순위를 min으로 두고, 해당 min보다 더 순위 높은 사람만 채용**<br/>

#### 문제해설 참고
[참고블로그](#http://blog.naver.com/PostView.nhn?blogId=occidere&logNo=220804048925&categoryNo=14&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView) <br/>
<img src="https://user-images.githubusercontent.com/62331803/92066226-5998de00-eddc-11ea-8c0f-1e7fd4fc58b2.png" width="50%"><br/>
<img src="https://user-images.githubusercontent.com/62331803/92066237-61588280-eddc-11ea-89bd-eb98b346660d.png" width="50%"><br/>

<br/>

## 전체코드

#### 내풀이(3차시도에 성공)

```python
import sys

score = []
input = sys.stdin.readline

cases = int(input())
for i in range(cases):
    num = int(input())
    score = [0 for i in range(num)]
    for j in range(num):
        rm, iv = map(int, input().split(' '))
        score[rm-1] = iv

    min = score[0]
    people = len(score)

    for i in range(1,num):
        iv = score[i]
        if iv > min:
            people -= 1
        else:
            min = iv

    print(people)
```

#### 1차시도 - 문제 이해 실수

```python

import sys

def newcomer(score):
    people = len(score)
    score = sorted(score,key= lambda x:x[0])
    print('서류 순으로 정렬:',score)

    rm = score[0][0]
    iv = score[0][1]
    for i in range(1,len(score)):
        next_rm = score[i][0]
        next_iv = score[i][1]
        if rm < next_rm and iv < next_iv:
            people -= 1
        rm = next_rm
        iv = next_iv

    return people

if __name__ =="__main__":
    score = []

    cases = int(sys.stdin.readline())
    for i in range(cases):
        num = int(sys.stdin.readline())
        for j in range(num):
            rm, iv = map(int, sys.stdin.readline().split(' '))
            score.append((rm,iv))

    print(newcomer(score))

```

#### 2차시도 

```python

import sys

def newcomer(score):
    people = len(score)
    score = sorted(score,key= lambda x:x[0])

    min = score[0][1]
    for i in range(1,len(score)):
        iv = score[i][1]
        if iv > min:
            people -= 1
        else:
            min = iv

    return people

if __name__ =="__main__":
    score = []

    cases = int(sys.stdin.readline())
    for i in range(cases):
        num = int(sys.stdin.readline())
        for j in range(num):
            rm, iv = map(int, sys.stdin.readline().split(' '))
            score.append((rm,iv))

    print(newcomer(score))


# 2차시도 수정! : case가 복수개인 경우 초기화 위치 주의
import sys

def newcomer(score):
    people = len(score)
    score = sorted(score,key= lambda x:x[0])

    min = score[0][1]
    for i in range(1,len(score)):
        iv = score[i][1]
        if iv > min:
            people -= 1
        else:
            min = iv

    return people

if __name__ =="__main__":
    cases = int(sys.stdin.readline())
    for i in range(cases):
        # score 위치 조정
        score = []
        num = int(sys.stdin.readline())
        for j in range(num):
            rm, iv = map(int, sys.stdin.readline().split(' '))
            score.append((rm,iv))

        # print문 위치 조정
        print(newcomer(score))

```
