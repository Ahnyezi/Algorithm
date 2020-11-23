# 문제이해
# k 개의 로프를 이용하여 w kg의 물체를 들어올림
# 각 로프는 고르게 k/w 를 부담

# 의사코드
# 로프가 감당할 수 있는 최대 무게가 담긴 방 max
# max 방을 오름차순으로 정렬하여
# 가장 첫번째 방 * 로프 개수를 구함

# 1차시도
# import sys
# rope = []
# max = []
#
# num = int(sys.stdin.readline())
# for i in range(num):
#     rope.append(int(sys.stdin.readline()))
#
# rope = sorted(rope)
#
# print(rope[0]*num)

# 2차시도
# 제약조건: 모든 로프를 사용할 필요 없다. 임의로 몇 개만 골라 사용 가능
# 고려할 사항: 1개 사용하는 경우, 2개 사용하는 경우, .... n개 사용하는 경우 나눈 뒤에
# 최대값 가져오기

# 1개 사용하는 경우: sorting해서 가장 큰 거 1개
# 2개 사용하는 경우: sorting해서 가장 큰 2개 중 작은거 * 2
# 3개 사용하는 경우: sorting해서 가장 큰 3개 중 가장 작은거 * 3

import sys
rope = []
max = []

num = int(sys.stdin.readline())
for i in range(num):
    rope.append(int(sys.stdin.readline()))

rope = sorted(rope, reverse=True)

for i in range(num):
    max.append(rope[i] * (i+1))

print(sorted(max)[num-1])
