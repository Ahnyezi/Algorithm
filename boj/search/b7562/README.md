# 백준 7562 | 나이트의 이동

![image](https://user-images.githubusercontent.com/62331803/99741009-7effd300-2b13-11eb-93b1-51ff94479aa3.png)

## 문제
![image](https://user-images.githubusercontent.com/62331803/99741046-9048df80-2b13-11eb-9850-3f52641fe5ee.png)


## 입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

## 출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.


## 입출력 예제
![image](https://user-images.githubusercontent.com/62331803/99741086-a6ef3680-2b13-11eb-84e1-3a9d7d8d0bd5.png)


# 풀이
- 나이트가 이동할 수 있는 경우의 수 dx,dy배열에 담기
   - `dx = [2,1,2,1,-2,-1,-2,-1]` 
   - `dy = [-1,-2,1,2,-1,-2,1,2]`
- x,y로 만들 수 있는 8가지의 새로운 x,y를 가지고, 새로운 x,y 방에 기존 x,y 방 값 +1 한 값을 삽입
   - `board[new_x][new_y] = board[x][y] + 1`
   - (주의) visited가 아직 False인 경우만!! 안하면 너무 느려
- 목표 지점의 방이 0이 아니게 되면 break 후에 출력
   - `print(board[goal_x][goal_y])`

```python
import sys
from collections import deque

input = sys.stdin.readline

dx = [2,1,2,1,-2,-1,-2,-1]
dy = [-1,-2,1,2,-1,-2,1,2]

count = []
T = int(input())
for _ in range(T):
    I = int(input())
    board = [[0 for _ in range(I)] for _ in range(I)]
    visited = [[False for _ in range(I)] for _ in range(I)] # 안해주면 짱 느려
    x, y = map(int,input().split()) # 순서 ? (상관 없나?)
    goal_x, goal_y = map(int,input().split()) # 순서 ?

    if x == goal_x and y == goal_y:
        print(0)
    else:
        queue = deque([[x, y]])
        visited[x][y] = True
        while queue:
            x, y = queue.popleft()
            for i in range(8):
                new_x = x + dx[i] #
                new_y = y + dy[i] #
                if 0 <= new_x < I and 0 <= new_y < I:
                    if not visited[new_x][new_y]:
                        board[new_x][new_y] = board[x][y] + 1
                        queue.append([new_x,new_y])
                        visited[new_x][new_y] = True
            if not board[goal_x][goal_y] == 0:
                break
        print(board[goal_x][goal_y])
```