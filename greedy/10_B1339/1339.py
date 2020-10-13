# 단어 수학

# 1차 (몰르게써)
# import sys
# input = sys.stdin.readline
# N = int(input())
#
# alpha = [0]*11
#
# for i in range(1,N+1):
#     alpha[i] = list(input().strip())
#
# for i in range(1,N+1):
#     max = i
#     for j in range(i+1,N+1):
#         if len(alpha[max]) < len(alpha[j]):
#             max = j
#     if max != i:
#         alpha[i],alpha[max] = alpha[max],alpha[i]
#
# print(alpha)
#
# nums = [9,8,7,6,5,4,3,2,1,0]
# for i in range(1,N+1):
#     for j in range(len(alpha[i])):
#         print('tmp 초기화')
#         tmp = str(nums.pop(0))
#         comp = alpha[i][j]
#         for k in range(1,N+1):
#             for l in range(0,len(alpha[k])):
#                 print(alpha[k][l])
#                 print(alpha[i][j])
#                 if alpha[k][l] == comp and alpha[k][l].isalpha():
#                     print('진입')
#                     alpha[k][l] = tmp
#         alpha[i][j] = tmp
#         print(alpha)
#
# print(alpha)

# 2차(알고리즘 참고)

# 1) 입력값의 알파벳 인덱스를 저장하는 배열 words 생성
# 2) 알파벳의 우선순위를 저장하는 배열 alphas 생성
# 3) 우선순위순으로 내림차순 정렬
# 4) 우선순위 높은 알파벳부터 숫자 부여 (9부터~0까지)

# import sys
# input = sys.stdin.readline
# N = int(input())
# words = [list(map(lambda x:ord(x)-65,input().rstrip())) for _ in range(N)]
#
# alpha = [0]*26
# for i in range(N):
#     j = 0
#     for w in words[i][::-1]:
#         alpha[w] += (10**j)
#         j += 1
#
# sorted(alpha,reverse=True)
#
# ans = 0
# cnt = 9
# for i in range(N):
#     if alpha[i] == 0:
#         break
#     ans += (alpha[i]*cnt)
#     cnt -= 1
#
# print(ans)

# 3차
# import sys
# input = sys.stdin.readline
# N = int(input())
# words = [list(map(lambda x:ord(x)-65,input().rstrip())) for _ in range(N)]
#
# alpha = [0]*26
# for i in range(N):
#     j = 0
#     for w in words[i][::-1]:
#         alpha[w] += (10**j)
#         j += 1
#
# sorted(alpha,reverse=True)
#
# ans = 0
# cnt = 9
# for i in range(26):
#     if alpha[i] == 0:
#         break
#     ans += (alpha[i]*cnt)
#     cnt -= 1
#
# print(ans)

# 4차
# - sort함수 잘못 사용
import sys
input = sys.stdin.readline
N = int(input())
words = [list(map(lambda x:ord(x)-65,input().rstrip())) for _ in range(N)]

alpha = [0]*26
for i in range(N):
    j = 0
    for w in words[i][::-1]:
        alpha[w] += (10**j)
        j += 1

alpha.sort(reverse=True)

ans = 0
cnt = 9
for i in range(26):
    if alpha[i] == 0:
        break
    ans += (alpha[i]*cnt)
    cnt -= 1

print(ans)
