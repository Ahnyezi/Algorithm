# 동물원
# 하나의 행이 추가되는 경우를 생각해보자
# 1) 추가되는 행에 사자가 (O,X) 일 경우
#    - 전 행은 (X,X) or (X,O)여야 한다.
# 2) 추가되는 행에 사자가 (X,O) 일 경우
#    - 전 행은 (X,X) or (O,X)여야 한다.
# 3) 추가되는 행에 사자가 (X,X) 일 경우
#    - 전 행은 (X,X) or (X,O) or (O,X)여야 한다.

# 리스트 사용
# import sys
# n = int(sys.stdin.readline())
# no = [1] + [0]*n
# left = [0]*(n+1)
# right = [0]*(n+1)
# mod = 9901
# 
# for i in range(1,n+1):
#     no[i] = (no[i-1] + left[i-1] + right[i-1]) % mod
#     left[i] = (no[i-1] + right[i-1]) % mod
#     right[i] = (no[i-1] + left[i-1]) % mod
# print((no[-1]+left[-1]+right[-1]) % mod)

# 변수 사용
import sys
n = int(sys.stdin.readline())
no, left, right = 1, 0, 0
mod = 9901

for i in range(n):
    no = (no + left + right) % mod
    left, right = no - right, no - left # 한 줄로 써줘야 돼

print((no + left + right) % mod)