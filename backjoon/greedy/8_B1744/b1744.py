# # # 문제이해
# # # 리스트 안의 수열의 합을 구하는 시행
# # # 숫자 두개를 묶어서 곱한뒤 합을 구함(1번 묶거나, 묶지 않을 수 있음)
# # # 합이 최대가 되게 짜라
# #
# # # N: 수열의 크기
# # # 수열 내의 숫자: -10000보다 크거나 같고, 10000보다 작거나 같은 정수
# # # 정답은 항상 2^31보다 작다
# #
# # # 입출력예제 힌트: 음수,0
# #
# # 분류
# # <양수만 있는 경우>
# # ex> 1 2 3 4==> 1+2+12=14 or 1+2+3+4=10
# # 공통: 0,1은 연산 x
# # 1) 짝수개
# # 1이 없다면, 1쌍씩 모두 곱셈 ex) 2 3 4 5 = (2*3) + (4*5)
# # 1이 있다면, 1과 1 다음 수까지 제외하고 나머지 곱셈 ex) 1 2 3 4 = 1 + 2 + (3*4)
# # 2) 홀수개
# # 1이 없다면, 맨 앞 빼고 그 다음 쌍부터 곱셈 ex) 2 3 4 = 2 + (3*4)
# # 1이 있다면, 1을 제외한 나머지 쌍 곱셈 ex) 1 2 3 4 5= 1 + (2*3) +(4*5) =
# # 통일 가능: 맨앞 빼고 그 다음부터 쌍 곱셈
# #
# # <음수가 포함된 경우>
# # ex> -4 -3 -2 -1 2
# # 1)음수 짝수개: 오름차순으로 정렬하여 앞부터 곱함.
# # 0 있다면, 연산 x
# # 2)음수 홀수: 짝수개까지만 곱하고 마지막 수는 연산 x
# # 0 있다면, 마지막 음수와 곱
#
def plus(sequence):
    length = len(sequence)
    sum = 0
    k = 0
    if length%2 == 1:
        sum = sequence[0]
        k = 1
    else:
        if 1 in sequence:
            sum = sequence[0] +sequence[1]
            k = 2
    for i in range(k,length,2):
        print(str(sum),end='+')
        sum+=sequence[i]*sequence[i+1]
        print("("+str(sequence[i]),"*",str(sequence[i+1])+")=",str(sum))
    return sum

def minus(sequence):
    # 0까지 배열이랑, 양수만 있는 배열로 나누기
    m = []
    p = []

    for i in sequence:
        if i <= 0:
            m.append(i)
        else:
            p.append(i)

    length = len(m)
    sum = 0
    l = len(m) - 1

    if length % 2 == 1:
        l -= 1
        sum = m[length-1]
        if 0 in m:
            sum = m[length-2] * 0
    else:
        if 0 in m:
            l -= 1

    for i in range(0,l,2):
        print(str(sum),end='+')
        sum+=m[i]*m[i+1]
        print("("+str(m[i]),"*",str(m[i+1])+")=",str(sum))

    return plus(p)+sum

import sys
input = sys.stdin.readline
sequence = []

num = int(input())
flag = True
for i in range(num):
    n = int(input())
    sequence.append(n)
    if not n > 0:
        flag = False

sequence = sorted(sequence) # [-1, 1, 2, 3]

if flag:
    print(plus(sequence))
else:
    print(minus(sequence))
