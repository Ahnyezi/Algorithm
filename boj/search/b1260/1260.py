# DFS와 BFS
# import sys
# from _collections import deque
#
# def bfs(start):
#     visited = [start]
#     queue = deque([start])
#     print('visited:',visited)
#     while queue:
#         n = queue.popleft()
#         print('<n:',end='')
#         print(n,end='')
#         print('>')
#         for i in range(len(matrix[start])):
#             print('i:',end='')
#             print(i)
#             if matrix[n][i] == 1 and (i not in visited):
#                 print('queue에 i 추가')
#                 visited.append(i)
#                 queue.append(i)
#                 print('visited:',end='')
#                 print(visited)
#                 print('queue:',end='')
#                 print(queue)
#         print()
#     return visited
#
# def dfs(start,visited):
#     print()
#     print('dfs(',end='')
#     print(start,end=',')
#     print(visited,end=')')
#     print()
#     visited += [start]
#     print('visited:',visited)
#     for i in range(len(matrix[start])):
#         print('i:',end='')
#         print(i)
#         if matrix[start][i] == 1 and (i not in visited):
#             print('조건 만족')
#             dfs(i,visited)
#     return visited
#
# input = sys.stdin.readline
# n, m, v = map(int,input().split())
#
# matrix = [[0]*(n+1) for _ in range(n+1)]
# for _ in range(m):
#     line = list(map(int, input().split()))
#     matrix[line[0]][line[1]] = 1
#     matrix[line[1]][line[0]] = 1
# print(matrix)
# # [[0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 1, 0]]
# # 1차원 인덱스 : 각 노드
# # 2차원 인덱스 : 각 노드에 연결된 인접노드 정보
#
# print('[dfs]')
# print(dfs(v,[]))
# print()
# print('[bfs]')
# print(bfs(v))

# 1차
# import sys
# from _collections import deque
#
# def bfs(start):
#     visited = [start]
#     queue = deque([start])
#     while queue:
#         n = queue.popleft()
#         for i in range(len(matrix[start])):
#             if matrix[n][i] == 1 and (i not in visited):
#                 visited.append(i)
#                 queue.append(i)
#     return visited
#
# def dfs(start,visited):
#     visited += [start]
#     for i in range(len(matrix[start])):
#         if matrix[start][i] == 1 and (i not in visited):
#             dfs(i,visited)
#     return visited
#
# input = sys.stdin.readline
# n, m, v = map(int,input().split())
#
# matrix = [[0]*(n+1) for _ in range(n+1)]
# for _ in range(m):
#     line = list(map(int, input().split()))
#     matrix[line[0]][line[1]] = 1
#     matrix[line[1]][line[0]] = 1
#
# print(dfs(v,[]))
# print(bfs(v))

# 2차 (성공)
import sys
from _collections import deque

def bfs(start):
    visited = [start]
    queue = deque([start])
    while queue:
        n = queue.popleft()
        for i in range(len(matrix[start])):
            if matrix[n][i] == 1 and (i not in visited):
                visited.append(i)
                queue.append(i)
    return visited

def dfs(start,visited):
    visited += [start]
    for i in range(len(matrix[start])):
        if matrix[start][i] == 1 and (i not in visited):
            dfs(i,visited)
    return visited

input = sys.stdin.readline
n, m, v = map(int,input().split())

matrix = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    line = list(map(int, input().split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1

print(*dfs(v,[]))
print(*bfs(v))