# 1. 리스트 정렬
#   <정렬방법>
#   1) 시작 시간을 기준으로 (x)
#   2) 회의 지속 시간을 기준으로 (x)
#   3) 종료 시간을 기준으로 (o)
# 2. 정렬된 리스트에서 하나씩 뽑아서 회의 배치

import sys

def greedy(meeting):
    end_time = 0 # 이전 회의의 종료시간
    meeting_count = 0

    for time in meeting:
        if end_time <= time[0]: # 이전 회의 종료시간 <= 현재 회의 시작시간
            meeting_count += 1
            end_time = time[1] # 현재 회의 종료시간
    return meeting_count

if __name__ == "__main__" :
    meeting = []
    mCount = int(sys.stdin.readline())
    for i in range(mCount):
        start, end = map(int, sys.stdin.readline().split())
        meeting.append((start,end))
    print(meeting)

    meeting = sorted(meeting, key=lambda time:time[0])
    print("시작시간으로 정렬:",meeting)
    meeting = sorted(meeting, key=lambda time:time[1])
    print("종료시간으로 정렬:",meeting)

    print('meeting_count:',greedy(meeting))

'''
<결과>
[(1, 4), (3, 5), (3, 4), (2, 2), (1, 2)]
시작시간으로 정렬: [(1, 4), (1, 2), (2, 2), (3, 5), (3, 4)]
종료시간으로 정렬: [(1, 2), (2, 2), (1, 4), (3, 4), (3, 5)]
3
'''