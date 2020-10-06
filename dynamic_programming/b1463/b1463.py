# 1로 만들기 (1h 26m)
# 10 이면
# 10 -> 5 -> 4 -> 2 -> 1 로 하지않고
# 큰 수로 나눔
# 1. 3의 배수로 만들기

# 1차시도
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# cnt = 0
#
# while True:
#     if x==1: break
#     if x%3 == 0:
#         x /= 3
#     elif x%2 == 0 and (x/2)%3 == 0:
#         x /= 2
#     else:
#         x -= 1
#     cnt += 1
#     print('cnt:'+str(cnt))
#     print('x:'+str(x))
#
# print(cnt)

# 문제 이해 자체가 잘못됨
# 큰 수로 나누는 것이 능사가 아니다!!!
# 최소값을 모두 계산하여 최소값으로 dp가 초기화되게 해야 함
# 점화식을 사용해서 풀자

# 2차시도
import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n+1)

for i in range(2,n+1):
    # print('i:'+str(i))
    d[i] = d[i-1]+1
    if i%2==0: d[i] = min(d[i],d[i//2]+1)
    if i%3==0: d[i] = min(d[i],d[i//3]+1)
    # print(d[i])

print(d[n])


