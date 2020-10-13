# 공주님의 정원

# 1) 입력받아서 리스트 형태로 저장
# 2) 각 리스트의 0번째방 순으로 오름차순 정렬
# 3) 3월 1일 포함하는 가장 늦게 시작하는 꽃 선택
# 4) 해당 꽃의 끝나는 날짜보다 먼저 시작하는 꽃 중 11월 30일 포함하는 꽃..

# import sys
# input = sys.stdin.readline
# N = int(input())
# flowers = [list(map(int,input().split())) for _ in range(N)]
#
# flowers.sort(key=lambda x:x[0])
# print(flowers)
#
# start = [3,1]
# end = [12,1] # 11,30 포함. 12,1에 지는 것으로 표시해야 함
# ans = 0
# for i in range(N):
#     if start[0] > flowers[i][0] or (start[0] == flowers[i][0] and start[1] >= flowers[i][1]):
#         #
#         start[0] = flowers[i][2]
#         start[1] = flowers[i][3]
#         ans += 1
#         print('start:',end='')
#         print(start)
#     if start[0] > end[0] or (start[0] == end[0] and start[1] >= end[1]):
#         print('break')
#         break
#
# print(ans)

# 2차 (예제 통과)==>틀림
# import sys
# input = sys.stdin.readline
# N = int(input())
# flowers = [list(map(int,input().split())) for _ in range(N)]
#
# flowers.sort(key=lambda x:x[0])
# # print(flowers)
#
# start = [3,1]
# end = [12,1] # 11,30 포함. 12,1에 지는 것으로 표시해야 함
# ans = 0
# for i in range(N):
#     for j in range(N):
#         if start[0] > flowers[j][0] or (start[0] == flowers[j][0] and start[1] >= flowers[j][1]):
#             # 이 상태에서 가장 늦게 끝나는 꽃
#             max = j
#     if start[0] > end[0] or (start[0] == end[0] and start[1] >= end[1]):
#         # print('break')
#         break
#     start[0] = flowers[max][2]
#     start[1] = flowers[max][3]
#     ans += 1
#     # print('start:', end='')
#     # print(start)
#
# print(ans)

# 3차 (틀림)
# import sys
# input = sys.stdin.readline
# N = int(input())
# flowers = [list(map(int,input().split())) for _ in range(N)]
#
# flowers.sort(key=lambda x:x[0])
# print(flowers)
#
# start = [3,1]
# end = [12,1] # 11,30 포함. 12,1에 지는 것으로 표시해야 함
# ans = 0
# for i in range(N):
#     for j in range(N):
#         if start[0] > flowers[j][0] or (start[0] == flowers[j][0] and start[1] >= flowers[j][1]):
#             # 이 상태에서 가장 늦게 끝나는 꽃
#             max = j
#     if start[0] > end[0] or (start[0] == end[0] and start[1] >= end[1]):
#         print('break')
#         break
#     start[0] = flowers[max][2]
#     start[1] = flowers[max][3]
#     ans += 1
#     print('start:', end='')
#     print(start)
#
# if ans < 2:
#     ans = 0
# print(ans)

# 4차 (모르겠다)
# import sys
# input = sys.stdin.readline
# N = int(input())
# flowers = [list(map(int,input().split())) for _ in range(N)]
#
# flowers.sort(key=lambda x:x[0])
# print(flowers)
#
# start = [3,1]
# end = [12,1] # 11,30 포함. 12,1에 지는 것으로 표시해야 함
# ans = 0
# for i in range(N):
#     for j in range(N):
#         if start[0] > flowers[j][0] or (start[0] == flowers[j][0] and start[1] >= flowers[j][1]):
#             # 이 상태에서 가장 늦게 끝나는 꽃
#             max = j
#     if start[0] > end[0] or (start[0] == end[0] and start[1] >= end[1]):
#         print('break')
#         break
#     start[0] = flowers[max][2]
#     start[1] = flowers[max][3]
#     ans += 1
#     print('start:', end='')
#     print(start)
#
# if ans < 2:
#     ans = 0
# print(ans)

# 5차 (다른 답안 참고)


