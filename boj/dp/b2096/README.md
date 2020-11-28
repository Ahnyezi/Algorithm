# 백준 2096 | 내려가기

<br>

[문제링크](https://www.acmicpc.net/problem/2096)

<br>

### :bulb: 풀이

**메모리 제한을 고려하여, **슬라이딩 윈도우 방식** 알고리즘을 사용한다.**<br>
<br>

- **이전 행과 다음 행을 연산하여 구한 최댓값들** : `tmax = [0,0,0]` 
- **이전 행과 다음 행을 연산하여 구한 최솟값들**: `tmin = [0,0,0]`
- **이전 시행에서 구한 각 자리에서의 최댓값들** : `a = [0,0,0]`
- **이전 시행에서 구한 각 자리에서의 최솟값들**`b = [0,0,0]`
<br>
<br>

**문제에서 주어진 규칙을 고려하여, 
`c`라는 새로운 행이 주어졌을 때 새로 만들어질 `tmax`와 `tmin`을 계산한다.**

> 테스트 케이스 풀이과정 <br>

<img src="https://user-images.githubusercontent.com/62331803/100495441-47d29700-318f-11eb-9ad5-bbac9aa39300.png" width="35%">
<br>

<img src="https://user-images.githubusercontent.com/62331803/100495464-7c465300-318f-11eb-9274-c1216e3db993.png" width="35%">
<br>

<img src="https://user-images.githubusercontent.com/62331803/100495465-7f414380-318f-11eb-9235-801384531418.png" width="35%">
<br>

<img src="https://user-images.githubusercontent.com/62331803/100495468-836d6100-318f-11eb-912d-e763f472ee66.png" width="35%">
<br>

<img src="https://user-images.githubusercontent.com/62331803/100495474-88caab80-318f-11eb-8165-f063fa5e9765.png" width="35%">
<br>

<img src="https://user-images.githubusercontent.com/62331803/100495476-8bc59c00-318f-11eb-8a09-6b0d4b7efc98.png" width="35%">
<br>
<br>
.<br>
.<br>
.<br>

<img src="https://user-images.githubusercontent.com/62331803/100495501-b1eb3c00-318f-11eb-9b6e-d1f28b8494a7.png" width="40%">
<br>


> 코드

```python
import sys
input = sys.stdin.readline
n = int(input())

res_max = [0,0,0]
res_min = [0,0,0]
prev_max = [0,0,0]
prev_min = [0,0,0]

for i in range(n):
    new = list(map(int,input().split()))
    res_max[0] = max(prev_max[0],prev_max[1]) + new[0]
    res_max[1] = max(prev_max[0],prev_max[1],prev_max[2]) + new[1]
    res_max[2] = max(prev_max[1],prev_max[2]) + new[2]
    res_min[0] = min(prev_min[0],prev_min[1]) + new[0]
    res_min[1] = min(prev_min[0],prev_min[1],prev_min[2]) + new[1]
    res_min[2] = min(prev_min[1],prev_min[2]) + new[2]
    prev_max = res_max[:] # deep copy
    prev_min = res_min[:]

print(max(res_max),min(res_min))
```









