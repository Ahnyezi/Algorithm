# 백준 1260 | DFS와 BFS
## 문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

## 입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

## 출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

## 입출력 예제
![image](https://user-images.githubusercontent.com/62331803/96400603-24b9dc80-120c-11eb-85b1-5e72499e2b4b.png)
<br>

![image](https://user-images.githubusercontent.com/62331803/96400613-2c798100-120c-11eb-8c95-0d022b6bdc5a.png)
<br>

![image](https://user-images.githubusercontent.com/62331803/96400623-313e3500-120c-11eb-9099-cd564be55865.png)

# 풀이

## 1차

```python
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
```

## 출력 예시 
```python
5 5 3
5 4
5 2
1 2
3 4
3 1

# matrix: [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0]]
```

> dfs
```python
[dfs]

dfs(3,[])
visited: [3]
i:0
i:1
조건 만족

dfs(1,[3])
visited: [3, 1]
i:0
i:1
i:2
조건 만족

dfs(2,[3, 1])
visited: [3, 1, 2]
i:0
i:1
i:2
i:3
i:4
i:5
조건 만족

dfs(5,[3, 1, 2])
visited: [3, 1, 2, 5]
i:0
i:1
i:2
i:3
i:4
조건 만족

dfs(4,[3, 1, 2, 5])
visited: [3, 1, 2, 5, 4]
i:0
i:1
i:2
i:3
i:4
i:5
i:5
i:3
i:4
i:5
i:2
i:3
i:4
i:5

[3, 1, 2, 5, 4]

```

> bfs
```python
[bfs]
visited: [3]
<n:3>
i:0
i:1
queue에 i 추가
visited:[3, 1]
queue:deque([1])
i:2
i:3
i:4
queue에 i 추가
visited:[3, 1, 4]
queue:deque([1, 4])
i:5

<n:1>
i:0
i:1
i:2
queue에 i 추가
visited:[3, 1, 4, 2]
queue:deque([4, 2])
i:3
i:4
i:5

<n:4>
i:0
i:1
i:2
i:3
i:4
i:5
queue에 i 추가
visited:[3, 1, 4, 2, 5]
queue:deque([2, 5])

<n:2>
i:0
i:1
i:2
i:3
i:4
i:5

<n:5>
i:0
i:1
i:2
i:3
i:4
i:5

[3, 1, 4, 2, 5]
```


# 피드백
- * 주의
   - `print(*dfs(v,[]))`