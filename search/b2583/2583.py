# 영역 구하기
# 0 2 4 4 -> ?
# 1 1 2 5 -> 3 1 0 1
# 4 0 6 2 -> 4 4 3 5 (3,4/3,5/4,4/4,5)
import sys
input = sys.stdin.readline
M,N,K = map(int,input().split()) # M:세로, N:가로, K:사각형 개수
paper = [[0 for _ in range(N)] for _ in range(M)]
for i in range(len(paper)):
    print(paper[i])
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split()) # 왼쪽 아래 x,y/오른쪽 위 x,y





