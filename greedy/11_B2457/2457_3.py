# 먼저 심을 수 있는 순서대로 정렬
# date = 100*M + D
import sys

flowers=[]

N=int(sys.stdin.readline())

for i in range(N):
    start_month, start_day, end_month, end_day=map(int, sys.stdin.readline().split())
    flowers.append((start_month*100+start_day, end_month*100+end_day))

print(flowers)
flowers.sort(key=lambda x:(x[0], x[1]))
print(flowers)
now = 301
ans = 0
index = 0
max = 0

for i in range(N):
    # 1번째 종료조건: 목표 달성
    if now > 1130:
        break

    # 오늘(now)을 포함하는 꽃들 중 가장 오래 심을 수 있는 꽃 찾기
    if max < flowers[i][1] and flowers[i][0] <= now:
        index = i
        max = flowers[i][1]

    # 오늘(now)을 포함하지 않은 꽃이 등장하면 오늘 날짜를 바꿔주고
    # 해당 꽃을 다시 봐야 하기 때문에 i에 1을 빼준다 ???
    if flowers[i][0] > now and max != 0:
        now = flowers[i][1]
        ans += 1
        i -= 1
        max = 0

    # 3번째 종료조건: 모든 꽃을 확인한 경우
    elif max != 0 and i == N-1:
        now = flowers[index][1]
        ans += 1

    # 2번째 종료조건: 꽃밭이 비어있는 날이 생길 경우
    elif max == 0:
        ans = 0
        break

# 모든 꽃을 확인하였지만 목표 달성 못한 경우
if now <= 1130:
    ans = 0

print(ans)