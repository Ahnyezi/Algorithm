# 공주님의 정원
# > 알고리즘
# - 월별 날짜를 100*M + D로 나타낸다.
# - 반복문 돌면서 꽃 선택
# - 모든 조건을 만족하면 반복문에서 나오기
# > 내부동작
# - flowers 배열을 0번째, 1번째방 기준 정렬 => 날짜가 빠른 순으로 정렬
# - 조건 만족시킬 때까지 외부 반복
# - 꽃 선택을 위한 내부 반복
# - 마지막으로 선택된 꽃의 enddate보다 startdate가 빠른 꽃 중
# 가장 늦게까지 피어있는 꽃을 선택 
# - 내부반복문에서 선택한 꽃을 selected 배열에 삽입 
# - 조건을 충족 못시킬 경우 selected 배열 초기화

# 1차 (틀림)
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

# 2차
# 반례
# 1
# 1 1 11 30
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