# 1,2,3 더하기
# 정수 n이 주어졌을 때, n을 1,2,3,의 합으로 나타내는 방법의 수
# 수를 '1'개 이상 사용!!!

# 점화식 구하기
# n=1 일때 0가지
# n=2 일때 2가지 1,1
# n=3 일때 3가지 1,1,1 / 1,2 / 2,1
# n=4 일때 7가지 1,1,1,1 / 2,1,1 / 1,2,1 / 1,1,2 / 2,2 / 1,3 / 3,1
# n=5 일때 13가지 (d[4]+6)
# 1,1,1,1,1 / 1,1,1,2 / 1,1,2,1/ 1,2,1,1,/ 2,1,1,1/ ==5
# 1,2,2/2,1,2/2,2,1/1,1,3/1,3,1/3,1,1/ ==6
# 1,4/4,1 ==2

# 몰르게써

# 알고리즘 참고하기
# n = 4일때
# 1의 경우의 수에 3을 더하기
# 2의 경우의 수에 2를 더하기
# 3의 경우의 수에 1을 더하기

# 2차시도 ==> 완전 틀렷다

# n = int(input())
# d = [0] * (n+1)
# d[1] = 1
# d[2] = 2
# for i in range(3,n+1):
#     for j in range(1,i+1):
#         d[i]+=d[j]
#         print(d[i])
#
# print(d[n])

# 3차 시도
# 전제가 틀림
# 1번째 방, 2번째 방, 3번째 방까지 구하고
# 4번째 방부터 for문을 통해서 구한다.

# n이 1부터 3까지는 4이상의 숫자 점화식으로 사용하기 위한 기본 항들
# n==1일때, 1 ==>1
# n==2일때, 1+1, 2 ==> 2
# n==3일때, 1+1+1, 2+1, 1+2, 3 ==> 4
# 따라서 n==4일때, 7가지
# 1,1,1,1 / 2,1,1 / 1,2,1 / 1,1,2 / 2,2 / 1,3 / 3,1

# import sys
# input = sys.stdin.readline
# while True:
#     n = input()
#     if n == '\n':
#         break
#     n = int(n)
#     d = [0] * (n+1)
#
#     d[1] = 1
#     d[2] = 2
#     d[3] = 4
#     for i in range(4,n+1):
#         for j in range(1,i):
#             d[i]+=d[j]
#             print(str(i)+":"+str(d[i]))
#         print()
#     print(d[n])

# 4차시도
# 1) 문제 잘읽기!!! 1,2,3만으로 연산
# 2) 문제 잘읽기!!! 테스트케이스 개수 먼저 받음

# import sys
#
# input = sys.stdin.readline
#
# tk = []
# N = int(input())
# for _ in range(N):
#     tk.append(int(input()))
#
# for n in tk:
#     d = [0] * (n+1)
#     d[1] = 1
#     d[2] = 2
#     d[3] = 4
#     for i in range(4,n+1):
#         d[i] = d[i-1]+d[i-2]+d[i-3]
#     print(d[n])

# 5차시도 (런타임 에러)
# import sys
#
# input = sys.stdin.readline
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     d = [0] * (n+1)
#     d[1] = 1
#     d[2] = 2
#     d[3] = 4
#     for i in range(4,n+1):
#         d[i] = d[i-1]+d[i-2]+d[i-3]
#     print(d[n])

# 6차시도
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    d = [0] * (n+1)
    if n < 3: ## 이거 왜..?
        print(n)
    else:
        d[1] = 1
        d[2] = 2
        d[3] = 4
        for i in range(4,n+1):
            d[i] = d[i-1]+d[i-2]+d[i-3]
        print(d[n])