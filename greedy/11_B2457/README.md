# 백준 2457 | 공주님의 정원 (어려버)
## 문제
![image](https://user-images.githubusercontent.com/62331803/95875291-d68c7f80-0dac-11eb-85af-34512a2769aa.png) <br>

## 입력
첫째 줄에는 꽃들의 총 개수 N (1<=N<=100,000)이 주어진다. 다음 N개의 줄에는 각 꽃이 피는 날짜와 지는 날짜가 주어진다. 하나의 날짜는 월과 일을 나타내는 두 숫자로 표현된다. 예를 들어서, 3 8 7 31은 꽃이 3월 8일에 피어서 7월 31일에 진다는 것을 나타낸다. 

## 출력
첫째 줄에 선택한 꽃들의 최소 개수를 출력한다. 만약 두 조건을 만족하는 꽃들을 선택할 수 없다면 0을 출력한다.

## 예제 입출력
![image](https://user-images.githubusercontent.com/62331803/95875395-f0c65d80-0dac-11eb-8ee8-acf6e99b372d.png)
<br>

# 풀이
## 1차 (알고리즘 대충 맞긴 한데 예제 틀림)
1) 입력받아서 리스트 형태로 저장
2) 각 리스트의 0번째방 순으로 오름차순 정렬
3) 3월 1일 포함하는 가장 늦게 시작하는 꽃 선택
4) 해당 꽃의 끝나는 날짜보다 먼저 시작하는 꽃 중 11월 30일 포함하는 꽃..

```python
import sys
input = sys.stdin.readline
N = int(input())
flowers = [list(map(int,input().split())) for _ in range(N)]

flowers.sort(key=lambda x:x[0])
print(flowers)

start = [3,1]
end = [12,1] # 11,30 포함. 12,1에 지는 것으로 표시해야 함
ans = 0
for i in range(N):
    for j in range(N):
        if start[0] > flowers[j][0] or (start[0] == flowers[j][0] and start[1] >= flowers[j][1]):
            # 이 상태에서 가장 늦게 끝나는 꽃
            max = j
    if start[0] > end[0] or (start[0] == end[0] and start[1] >= end[1]):
        print('break')
        break
    start[0] = flowers[max][2]
    start[1] = flowers[max][3]
    ans += 1
    print('start:', end='')
    print(start)

if ans < 2:
    ans = 0
print(ans)
```

## 2차 (알고리즘 참고) ==> 마지막에서 채점 오류
> 알고리즘
- 월별 날짜를 100*M + D로 나타낸다.
- 반복문 돌면서 꽃 선택
- 모든 조건을 만족하면 반복문에서 나오기
> 내부동작
- flowers 배열을 0번째, 1번째방 기준 정렬 => 날짜가 빠른 순으로 정렬
- 조건 만족시킬 때까지 외부 반복
- 꽃 선택을 위한 내부 반복
- 마지막으로 선택된 꽃의 enddate보다 startdate가 빠른 꽃 중
가장 늦게까지 피어있는 꽃을 선택 
- 내부반복문에서 선택한 꽃을 selected 배열에 삽입 
- 조건을 충족 못시킬 경우 selected 배열 초기화

```python
import sys
input = sys.stdin.readline
N = int(input())
flowers = []
for _ in range(N):
    start_month, start_day, end_month, end_day = map(int, input().split())
    flowers.append([100*start_month+start_day,100*end_month+end_day])
# print(flowers)

flowers.sort(key=lambda x:(x[0],x[1]))
print(flowers)

princess_start = 100 * 3 + 1
princess_end = 100 * 11 + 30

selected = []
lastidx = -1
f = [0, 0]
for _ in range(N):
    flag = False

    if f[1] > princess_end: # 마지막으로 선택된 꽃의 지는 날 >= 11/30
        print('조건 만족')
        break

    for i in range(lastidx + 1,N):
        if flowers[i][0] <= princess_start and flowers[i][1] > f[1]:
            f = flowers[i]
            lastidx = i
            flag = True
    if flag:
        selected.append(f)
        princess_start = f[1]
    else:
        selected = []
        break
    print(selected)

print(selected)
print(len(selected))

```

## 3차
- 반례: 1, 1 1 11 30
- for문 사용할 경우 1번 반복 후에 빠져나오기 때문에 selected=[]처리 불가
- 따라서 외부반복문 while문으로 변경
```python
import sys
input = sys.stdin.readline
N = int(input())
flowers = []
for _ in range(N):
    start_month, start_day, end_month, end_day = map(int, input().split())
    flowers.append([100*start_month+start_day,100*end_month+end_day])

flowers.sort(key=lambda x:(x[0],x[1]))

princess_start = 100 * 3 + 1
princess_end = 100 * 11 + 30

selected = []
lastidx = -1
f = [0, 0]
while True:
    flag = False
    if f[1] > princess_end: # 마지막으로 선택된 꽃의 지는 날 > 11/30
        break

    for i in range(lastidx + 1,N):
        if flowers[i][0] <= princess_start and flowers[i][1] > f[1]:
            f = flowers[i]
            lastidx = i
            flag = True
    if flag:
        selected.append(f)
        princess_start = f[1]
    else:
        selected = []
        break

print(len(selected))
```

### 다른 답안
```python
import sys

accumulation={1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334}

def md_to_d(month, day):
    return accumulation[month]+day

flowers=[]

N=int(sys.stdin.readline())

for i in range(N):
    start_month, start_day, end_month, end_day=map(int, sys.stdin.readline().split())
    flowers.append((md_to_d(start_month, start_day), md_to_d(end_month, end_day)))

startdate=60 # 3월 1일까지
enddate=334 # 11월 30일까지
flowers.sort(key=lambda x:(x[0], x[1])) # x[0]으로 정렬한 후, x[1]으로 한번 더 정렬

print(flowers)

selected=[]
end=60 # 마지막으로 선택된 꽃의 end date

x=-1
temp=0
changed=0
selected=[]

# 마지막 꽃의 end 값이 enddate보다 적거나 같을 때
# flowers의 배열 개수이하로 반복
while end<=enddate and x<N:
    changed=0
    x+=1
    
    for i in range(x, N):
        if flowers[i][0]>end:
            break
        if temp<flowers[i][1]: # 조건 중 end date 가장 큰 flower 찾기
            temp=flowers[i][1]
            x=i # flower 인덱스
            changed=1
            
    # end 값 초기화
    if changed==1:
        end=temp
        selected.append(flowers[x]) # 최대 idx의 flower 삽입

    else: # 안넣으면 마지막에 틀림
        selected=[]
        break

print(len(selected))

```


