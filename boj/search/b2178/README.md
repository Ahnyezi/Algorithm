# 백준 2178 | 미로 탐색

![image](https://user-images.githubusercontent.com/62331803/98457921-c5c60280-21ce-11eb-9e9d-d5d3e023c029.png)
<br>

## 문제

![image](https://user-images.githubusercontent.com/62331803/98457930-d5454b80-21ce-11eb-9c30-591b76767575.png)
<br>

## 입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

## 출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다

## 입출력 예제

![image](https://user-images.githubusercontent.com/62331803/98457943-00c83600-21cf-11eb-9229-e1121c6d57a5.png)
<br>

![image](https://user-images.githubusercontent.com/62331803/98457947-09b90780-21cf-11eb-8247-ffd7d6c2601f.png)
<br>

![image](https://user-images.githubusercontent.com/62331803/98457951-12114280-21cf-11eb-8626-c1e8fa51b5e9.png)
<br>

![image](https://user-images.githubusercontent.com/62331803/98457954-19385080-21cf-11eb-9312-a8a03265f9da.png)
<br>

# 풀이
## 1차 (모르겠오)

```python
N,M = map(int,input().split())
maze = [0]*N
for i in range(N):
    maze[i] = list(map(int,list(input())))
# print(maze)
visited = [[0]*M]*N
dx = [-1,0,1,0]
dy = [0,-1,0,1]
cnt = 0

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            if 0 <= i < M and 0 <= j < N:
                visited[i][j] = 1

```

## 2차 (알고리즘 참고)
- 최단거리를 dfs로 풀면 시간복잡도 큼. -> 경로가 아주 많을 수 있기 때문.
- 따라서, 최단거리 문제는 bfs로 풀어야 한다. -> bfs 알고리즘을 따라가면 가장 먼저 끝나는 거리가 자동적으로 최단거리가 됨

```python
N,M = map(int,input().split())
maze = [0]*N
for i in range(N):
    maze[i] = list(map(int,list(input())))
dx = [1,-1,0,0]
dy = [0,0,-1,1]
queue = [[0,0]]
# print(maze)
while queue:
    x,y = queue[0][0],queue[0][1]
    del queue[0]
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        ## N과 M의 위치?
        if 0 <= new_x < N and 0 <= new_y < M and maze[new_x][new_y] == 1:
            queue.append([new_x,new_y])
            maze[new_x][new_y] = maze[x][y]+1
# print(maze)
print(maze[N-1][M-1])

```

# 피드백
- `if 0 <= new_x < N and 0 <= new_y < M`
   - N과 M의 위치 이해 안됨...
   - N과 M 위치 바꿀 경우 런타임 에러

