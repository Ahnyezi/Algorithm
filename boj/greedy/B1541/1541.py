# 잃어버린 괄호
# 괄호를 쳐서 결과를 최소로 만들기

# 0~9/+/- 로만 이루어짐
# 가장 처음과 마지막 문자는 숫자
# 연속 2개 이상의 연산자 X
# 5자리가 넘어가는 숫자는 없음
# 수는 0으로 시작 가능

# 1차시도(못풂)
# '-'가 오면 묶고 다음 -에서 감싸줌
# import sys
# expression = sys.stdin.readline().rstrip()
# minus = []
# for idx, w in enumerate(expression):
#     if w == '-':
#         minus.append(idx)
#
# print(minus)
#
# for i in range(len(minus)):
#     expression = expression[:minus[i]+1] + '(' + expression[minus[i]+1:]
#     for j in range(i+1,len(minus)):
#         minus[j] += 1
#
# if len(minus) % 2 == 1:
#     expression += ')'
#
# print(expression)


# 2차 (다른 답안 참고)
# - '-'를 기준으로 나눈 뒤에
# - 나눠진 배열방 값 연산하여
# 결과값에 다시 마이너스 연산

import sys
expression = sys.stdin.readline().split('-')
results = []

for w in expression:
    res = 0
    nums = w.split('+')
    for n in nums:
        res += int(n)
    results.append(res)

ans = results[0]
for i in range(1,len(results)):
    ans -= results[i]
print(ans)