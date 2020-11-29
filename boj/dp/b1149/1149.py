# RGB 거리
# 1번 집이 R을 선택했을 때 -> 뒤부터 min()
# 1번 집이 G를 선택했을 때
# 1번 집이 B를 선택했을 때

# 배열
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# r = [0] * n
# g = [0] * n
# b = [0] * n
# r[0],g[0],b[0] = map(int,input().split())
#
# for i in range(1,n):
#     x,y,z = map(int,input().split())
#     r[i] = x + min(g[i-1],b[i-1])
#     g[i] = y + min(r[i-1],b[i-1])
#     b[i] = z + min(r[i-1],g[i-1])
#
# print(min(r[-1],g[-1],b[-1]))

# 슬라이딩 윈도우
import sys
input = sys.stdin.readline
n = int(input())

r, g, b = map(int,input().split())
for i in range(1,n):
    x,y,z = map(int,input().split())
    newr = x + min(g,b)
    newg = y + min(r,b)
    newb = z + min(r,g)
    r,g,b = newr,newg,newb

print(min(r,g,b))
# print(r,g,b)
