# 문제이해
# 다른 지원자들과 비교해서 서류심사, 면접시험 성적중
# 적어도 하나가 다른 지원자보다 떨어지지 않는자만 선발
# 예를 들어 A와 B를 비교했을 때,
# A(7,3) B(4,2)라면 A[0]>B[0]이면서 A[1]>B[1]이기 때문에
# B는 조건에 맞지 않는다.

# 의사코드
# 서류 심사로 정렬해서 뒤에 사람 값과 비교
# 조건에 맞지 않으면, people 수를 하나씩 줄여간다.

# 1차시도

# import sys
#
# def newcomer(score):
#     people = len(score)
#     score = sorted(score,key= lambda x:x[0])
#     print('서류 순으로 정렬:',score)
#
#     rm = score[0][0]
#     iv = score[0][1]
#     for i in range(1,len(score)):
#         next_rm = score[i][0]
#         next_iv = score[i][1]
#         if rm < next_rm and iv < next_iv:
#             people -= 1
#         rm = next_rm
#         iv = next_iv
#
#     return people
#
# if __name__ =="__main__":
#     score = []
#
#     cases = int(sys.stdin.readline())
#     for i in range(cases):
#         num = int(sys.stdin.readline())
#         for j in range(num):
#             rm, iv = map(int, sys.stdin.readline().split(' '))
#             score.append((rm,iv))
#
#     print(newcomer(score))

# 2차시도 :  왜?
# import sys
#
# def newcomer(score):
#     people = len(score)
#     score = sorted(score,key= lambda x:x[0])
#
#     min = score[0][1]
#     for i in range(1,len(score)):
#         iv = score[i][1]
#         if iv > min:
#             people -= 1
#         else:
#             min = iv
#
#     return people
#
# if __name__ =="__main__":
#     score = []
#
#     cases = int(sys.stdin.readline())
#     for i in range(cases):
#         num = int(sys.stdin.readline())
#         for j in range(num):
#             rm, iv = map(int, sys.stdin.readline().split(' '))
#             score.append((rm,iv))
#
#         print(newcomer(score))


# 2차시도 수정! : case가 복수개인 경우 초기화 위치 주의
import sys

def newcomer(score):
    people = len(score)
    score = sorted(score,key= lambda x:x[0])

    min = score[0][1]
    for i in range(1,len(score)):
        iv = score[i][1]
        if iv > min:
            people -= 1
        else:
            min = iv

    return people

if __name__ =="__main__":
    cases = int(sys.stdin.readline())
    for i in range(cases):
        # score 위치 조정
        score = []
        num = int(sys.stdin.readline())
        for j in range(num):
            rm, iv = map(int, sys.stdin.readline().split(' '))
            score.append((rm,iv))

        # print문 위치 조정
        print(newcomer(score))


# 최종
import sys

score = []
input = sys.stdin.readline

cases = int(input())
for i in range(cases):
    num = int(input())
    score = [0 for i in range(num)]
    for j in range(num):
        rm, iv = map(int, input().split(' '))
        score[rm-1] = iv

    min = score[0]
    people = len(score)

    for i in range(1,num):
        iv = score[i]
        if iv > min:
            people -= 1
        else:
            min = iv

    print(people)