# 텀 프로젝트
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# T = int(input())
#
# def bfs(i):
#     print('bfs 호출',end='>>')
#     print(i)
#     same_team = []
#     same_team.append(i)
#     # print(i,student[i])
#     queue.append([i,student[i]])
#     visited[i] == 1
#     while queue:
#         choose, chosen = queue.popleft()
#         if choose == student[chosen]:
#         # if choose == student[chosen] and visited[student[chosen]] == 0:
#             same_team.append(chosen)
#             visited[chosen] == 1
#             queue.append([chosen,student[chosen]])
#             print('여기니?')
#         elif choose != student[chosen]:
#             print('일치 x')
#             print(queue)
#         print('queue:',queue)
#     if len(same_team) == 1:
#         same_team.clear()
#     print('same_team:',same_team)
#     print()
#     return same_team
#
# for _ in range(T):
#     n = int(input())
#     student = list(map(int,input().split()))
#     student.insert(0,0)
#     visited = [0]*(n+1)
#     visited[0] = 1
#     queue = deque()
#     team = []
#     for i in range(n):
#         same_team = bfs(i)
#         if same_team: # 2명 이상
#            team.append(same_team)
#     print('team:',team)


## 2차 (dfs) 식빵
# import sys
#
# input = sys.stdin.readline
# T = int(input())
#
# def dfs(i):
#     same_team = []
#     same_team.append(i)
#     stack = []
#     stack.append([i,student[i]])
#
#     while stack:
#         choose, chosen = stack.pop()
#         visited[choose] = 1
#
#     return same_team
#
# for _ in range(T):
#     n = int(input())
#     student = list(map(int,input().split()))
#     student.insert(0,0)
#     visited = [0]*(n+1)
#     visited[0] = 1
#     team = []
#     for i in range(n):
#         same_team = dfs(i)
#         if same_team: # 2명 이상
#            team.append(same_team)
#     print('team:',team)

# 3차 (답지 참고)
# - 재귀 사용 x
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    student = [0] + list(map(int,input().split()))
    visited = [0] * (n+1)

    group = 1
    for i in range(1,n+1):
        if visited[i] == 0:
            while visited[i] == 0:
                visited[i] = group
                i = student[i]
            while visited[i] == group:
                visited[i] = -1
                i = student[i]
            group += 1
    cnt = 0
    for v in visited:
        if v > 0: # -1과 0빼고 카운트
            cnt += 1
    sys.stdout.write("{}\n".format(cnt))

# - 재귀 사용 (https://claude-u.tistory.com/435)