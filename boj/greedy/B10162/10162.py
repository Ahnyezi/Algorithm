# 전자레인지

# 1차
# import sys
# input = sys.stdin.readline
#
# btns = [60*5,60*1,10]
# cnts = [0,0,0]
#
# T = int(input())
#
# flag = True
# for _ in range(1000):
#     for i in range(2,-1,-1):
#         if T == 0:
#             print(str(cnts[0])+' '+str(cnts[1])+' '+str(cnts[2]))
#             flag = False
#             break
#         if T < 0:
#             print(-1)
#             flag = False
#             break
#         if btns[i] <= T:
#             T -= btns[i]
#             cnts[i] += 1
#     if not flag:
#         break

# 2차 (성공)
# import sys
# input = sys.stdin.readline
#
# btns = [60*5,60*1,10]
# cnts = [0,0,0]
#
# T = int(input())
#
# flag = True
# for _ in range(1000):
#     for i in range(3):
#         if T == 0:
#             print(str(cnts[0])+' '+str(cnts[1])+' '+str(cnts[2]))
#             flag = False
#             break
#         if btns[2] > T:
#             print('-1')
#             flag = False
#             break
#         if btns[i] <= T:
#             T -= btns[i]
#             cnts[i] += 1
#             break
#     if not flag:
#         break

# 다른 답안
import sys
input = sys.stdin.readline

T = int(input())
A,B,C = 0,0,0

if T % 10:
    print('-1')
else:
    A = int(T/300)
    T %= 300
    B = int(T/60)
    T %= 60
    C = int(T/10)
    T %= 10
    print(str(A)+' '+str(B)+' '+str(C))
