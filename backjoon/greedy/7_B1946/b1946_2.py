'''
서류심사 성적을 기준으로
오름차순으로 설정한다.

그리고 면접성적만 확인하면서
검사를 해나가는데

min보다 작은 값이 있다면
min에 저장해주고

min보다 크다면
cnt를 증가시켜준다.

서류 순으로 정렬: [(1, 4), (2, 5), (3, 6), (4, 2), (5, 7), (6, 1), (7, 3)]
3
'''

import sys

input = sys.stdin.readline

test = int(input())
for i in range(test):
    n = int(input())
    score = [0 for i in range(n+1)]
    for j in range(n):
        rm, iv = map(int, input().split())
        score[rm] = iv # 각 사람의 면접 순위를 서류심사 순으로 오름차순 정렬
                        # 가장 앞에 있는 사람이 1등 (무조건 합격)
    min = score[1]
    cnt = 0
    print('score:',score)
    for k in range(2, n+1):
        if score[k] > min:
            cnt += 1
        else:
            min = score[k]

    print(n-cnt)
