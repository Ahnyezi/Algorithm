# 너비 우선 탐색
# - 너비를 우선으로 하여 탐색을 수행
# - '최단 경로'를 찾아주기 때문에, 최단 길이 보장에 사용
# - queue로 구현

from collections import deque

graph = {
    1 : set([2,3]),
    2 : set([1,3,4,5]),
    3 : set([1,2,6,7]),
    4 : set([2,5]),
    5 : set([2,4]),
    6 : set([3,7]),
    7 : set([3,6])
}

def bfs(start):
    visited = []
    queue = deque([start])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

print(bfs(1))

# def bfs(start):
#     visited = []
#     queue = deque([start])
#     print(queue)
#
#     while queue:
#         n = queue.popleft()
#         print('n:'+str(n))
#         if n not in visited:
#             print('not yet visited')
#             visited.append(n)
#             print('graph[n]:',graph[n])
#             print('set(visited):',set(visited))
#             queue += graph[n] - set(visited)
#             print('=> queue: ',end='')
#             print(queue)
#         print()
#     return visited
#
# print(bfs(1))

