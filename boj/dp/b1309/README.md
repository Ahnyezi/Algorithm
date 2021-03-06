# 백준 1309 | 동물원

<br>

[문제링크](https://www.acmicpc.net/problem/1309)

<br>

:bulb: **풀이**
**하나의 행이 추가되는 경우를 생각해보자**<br>
1)  `(X,X)` : 추가되는 행에 사자가 없는 경우
   - 전 행은 `(X,X)` or `(X,O)` or `(O,X)`여야 한다.
   - 따라서 이전 행의 `사자가 없는 경우의 값`, `오른쪽에 있는 경우의 값`, `왼쪽에 있는 경우의 값`을 모두 더하여 삽입한다.

<img src="https://user-images.githubusercontent.com/62331803/100492384-c5d27600-316e-11eb-8215-a581ee94416b.png" width="30%">

<br>

2) `(O,X)`: 추가되는 행의 왼쪽에 사자가 있을 경우
   - 전 행은 `(X,X)` or `(X,O)`여야 한다.
   - 따라서 이전 행의 `사자가 없는 경우의 값`, `오른쪽에 있는 경우의 값`을 더하여 삽입한다.

<img src="https://user-images.githubusercontent.com/62331803/100492411-08944e00-316f-11eb-87f7-6221a95c23ff.png" width="30%">

<br>

3) `(X,O)`: 추가되는 행의 오른쪽에 사자가 있을 경우
   - 전 행은 `(X,X)` or (O,X)여야 한다.
   - 따라서 이전 행의 `사자가 없는 경우의 값`,  `왼쪽에 있는 경우의 값`을 모두 더하여 삽입한다.

<img src="https://user-images.githubusercontent.com/62331803/100492416-1649d380-316f-11eb-9c2c-166b7e7adb41.png" width="30%">

<br>
<br>
<br>


> 코드 
#### 배열 O 풀이

```python
import sys
n = int(sys.stdin.readline())
no = [1] + [0]*n
left = [0]*(n+1)
right = [0]*(n+1)
mod = 9901

for i in range(1,n+1):
    no[i] = (no[i-1] + left[i-1] + right[i-1]) % mod
    left[i] = (no[i-1] + right[i-1]) % mod
    right[i] = (no[i-1] + left[i-1]) % mod
print((no[-1]+left[-1]+right[-1]) % mod)

```


#### 배열 X 풀이
```python
import sys
n = int(sys.stdin.readline())
no, left, right = 1, 0, 0
mod = 9901

for i in range(n):
    no = (no + left + right) % mod
    left, right = no - right, no - left # 주의

print((no + left + right) % mod)
```

<br>

> 속도 비교<br>

- `위`: 배열 X, `아래`: 배열 O

<img src="https://user-images.githubusercontent.com/62331803/100492353-928fe700-316e-11eb-84b8-b3005281d5f5.png" width="40%">




