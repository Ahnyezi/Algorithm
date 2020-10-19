# 깊이 우선 탐색
# - 보다 깊은 것을 우선적으로 탐색
# - 너비 우선 : queue, 깊이 우선 : stack
# - 하지만, stack 사용하지 않아도 재귀로 구현 가능
#     - 컴퓨터는 구조적으로 항상 stack의 원리를 사용
#     - 따라서, stack에 담고 빼는 것과 동일한 효과를 낸다.

graph = {
    1 : set([2,3]),
    2 : set([1,3,4,5]),
    3 : set([1,2,6,7]),
    4 : set([2,5]),
    5 : set([2,4]),
    6 : set([3,7]),
    7 : set([3,6])
}

def dfs(start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n]-set(visited)
    return visited

print(dfs(1))