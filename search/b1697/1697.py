# 숨바꼭질
# 수빈이 : N, 수빈이 동생 : K (0 <= N,K <= 100,000)
# 수빈이가 X일 경우, x+1/x-1 or 2*x로 이동 가능
# 가장 빠른 시간 => bfs

# (예시1)
# 5, 17
# 5 -> 10 -> 9 -> 18 -> 17

# 1차 (알고리즘 참고)
# queue배열에 연산 결과와 횟수를 함께 저장
# queue가 아닌 다른 배열 만들어서 연산 결과 따로 저장할 필요 없음.

from collections import deque
N,K = map(int,input().split()) # N:기준점, K:목표지점
visited = [0 for i in range(100001)] # 최대값크기의 배열
queue = deque()
queue.append([N,0]) # 기준점, 횟수

while queue:
    point, cnt = queue.popleft()
    if point == K:
        print(cnt)
        break
    visited[point] = 1
    if point-1 >= 0 and visited[point-1] == 0:
        queue.append([point-1,cnt+1])
    if point+1 <= 100000 and visited[point+1] == 0:
        queue.append([point+1,cnt+1])
    if point*2 <= 100000 and visited[point*2] == 0:
        queue.append([point*2,cnt+1])
