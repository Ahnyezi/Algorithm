# 백준 1339 | 단어 수학
## 문제 
![image](https://user-images.githubusercontent.com/62331803/95766535-5e5f8480-0cee-11eb-955c-1ddcd8985545.png)

## 입력
첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다. 둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다. 단어는 알파벳 대문자로만 이루어져있다. 모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 수의 최대 길이는 8이다. 서로 다른 문자는 서로 다른 숫자를 나타낸다.

## 출력
첫째 줄에 주어진 단어의 합의 최댓값을 출력한다.

## 입출력 예제
![image](https://user-images.githubusercontent.com/62331803/95766604-76370880-0cee-11eb-9067-9fe35d7112c6.png)
<br>

![image](https://user-images.githubusercontent.com/62331803/95766617-7cc58000-0cee-11eb-92cb-1a60341b7d2d.png)
<br>

![image](https://user-images.githubusercontent.com/62331803/95766629-8222ca80-0cee-11eb-92fa-26a7a5e90c37.png)
<br>

![image](https://user-images.githubusercontent.com/62331803/95766637-86e77e80-0cee-11eb-831d-20bd33c2033b.png)

# 풀이 
## 1차 (알고리즘 생각 못함)
```python
import sys
input = sys.stdin.readline
N = int(input())

alpha = [0]*11

for i in range(1,N+1):
    alpha[i] = list(input().strip())

for i in range(1,N+1):
    max = i
    for j in range(i+1,N+1):
        if len(alpha[max]) < len(alpha[j]):
            max = j
    if max != i:
        alpha[i],alpha[max] = alpha[max],alpha[i]

print(alpha)

nums = [9,8,7,6,5,4,3,2,1,0]
for i in range(1,N+1):
    for j in range(len(alpha[i])):
        print('tmp 초기화')
        tmp = str(nums.pop(0))
        comp = alpha[i][j]
        for k in range(1,N+1):
            for l in range(0,len(alpha[k])):
                print(alpha[k][l])
                print(alpha[i][j])
                if alpha[k][l] == comp and alpha[k][l].isalpha():
                    print('진입')
                    alpha[k][l] = tmp
        alpha[i][j] = tmp
        print(alpha)

print(alpha)
```

## 2차 (알고리즘 참고) ==> 틀림 (range 오류)
1) 입력값의 알파벳 인덱스를 저장하는 배열 words 생성
2) 알파벳의 우선순위를 저장하는 배열 alphas 생성
3) 우선순위순으로 내림차순 정렬
4) 우선순위 높은 알파벳부터 숫자 부여 (9부터~0까지)


```python
import sys
input = sys.stdin.readline
N = int(input())
words = [list(map(lambda x:ord(x)-65,input().rstrip())) for _ in range(N)]

alpha = [0]*26
for i in range(N):
    j = 0
    for w in words[i][::-1]:
        alpha[w] += (10**j)
        j += 1

sorted(alpha,reverse=True)

ans = 0
cnt = 9
for i in range(N):
    if alpha[i] == 0:
        break
    ans += (alpha[i]*cnt)
    cnt -= 1

print(ans)
```

## 3차 (range N => 26) 틀림
```python 
import sys
input = sys.stdin.readline
N = int(input())
words = [list(map(lambda x:ord(x)-65,input().rstrip())) for _ in range(N)]

alpha = [0]*26
for i in range(N):
    j = 0
    for w in words[i][::-1]:
        alpha[w] += (10**j)
        j += 1

sorted(alpha,reverse=True)

ans = 0
cnt = 9
for i in range(26):
    if alpha[i] == 0:
        break
    ans += (alpha[i]*cnt)
    cnt -= 1

print(ans)
```

## 4차 (정답)
- sort함수 잘못 사용'
- 변경 전 :
`sorted(alpha,reverse=True)`
- 변경 후 :
`alpha.sort(reverse=True)`
```python
import sys
input = sys.stdin.readline
N = int(input())
words = [list(map(lambda x:ord(x)-65,input().rstrip())) for _ in range(N)]

alpha = [0]*26
for i in range(N):
    j = 0
    for w in words[i][::-1]:
        alpha[w] += (10**j)
        j += 1

alpha.sort(reverse=True)

ans = 0
cnt = 9
for i in range(26):
    if alpha[i] == 0:
        break
    ans += (alpha[i]*cnt)
    cnt -= 1

print(ans)
```

# 피드백
- 알고리즘 아이디어 어렵따.
    - 받아온 알파벳의 인덱스를 뽑아와
    - 모든 알파벳의 우선순위를 구한다
- map(), lambda() 사용법
    - `[list(map(lambda x:ord(x)-65,input().rstrip())) for _ in range(N)]`
- 내림차순 정렬 함수 사용법
    - `alpha.sort(reverse=True)`
