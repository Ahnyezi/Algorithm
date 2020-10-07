# 피보나치 함수
# 재귀함수로 피보나치 수열 구할 경우,
# fibonacci(3) ==> return fibo(2) + fibo(1)

# fibo(2) ==> return fibo(1) + fibo(0)
# fibo(1) ==> print('1'), return 1

# fibo(1) ==> print('1'), return 1
# fibo(0) ==> print('0'), return 0

# 즉, 1은 2번 호출되고, 0은 한번 호출됨.

# fibo(4)일 경우
# return fibo(3) + fibo(2)

# fibo(3) ==> return fibo(2) + fibo(1)
# fibo(2) ==> return fibo(1) + fibo(0)

# fibo(2) ==> return fibo(1) + fibo(0)
# fibo(1) ==> print('1'), return 1
# fibo(1) ==> print('1'), return 1
# fibo(0) ==> print('0'), return 0

# fibo(1) ==> print('1'), return 1
# fibo(0) ==> print('0'), return 0

# 즉, 1은 3번 호출되고, 0은 2번 호출됨.

# fibo(5)일 경우
# return fibo(4) + fibo(3)

# fibo(0) 일 때, 1 0
# fibo(1) 일 때, 0 1
# fibo(2) 일 때, 1 1
# fibo(3) 일 때, 1 2
# fibo(4) 일 때, 2 3  즉, 바로 앞결과 + 앞앞 결과


# 1차시도 (23m)
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    # d = [0]*(N+1)
    d = [(1,0),(0,1)]
    for i in range(2,N+1):
        d.append((d[i-1][0]+d[i-2][0],d[i-1][1]+d[i-2][1]))
    print(str(d[N][0])+" "+str(d[N][1]))

