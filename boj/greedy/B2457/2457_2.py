import sys

accumulation={1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334}

def md_to_d(month, day):
    return accumulation[month]+day

flowers=[]

N=int(sys.stdin.readline())

for i in range(N):
    start_month, start_day, end_month, end_day=map(int, sys.stdin.readline().split())
    flowers.append((md_to_d(start_month, start_day), md_to_d(end_month, end_day)))
print(flowers) # [(1, 151), (1, 181), (135, 243), (161, 344)]

# 기준
startdate=60 # 3월 1일까지
enddate=334 # 11월 30일까지
flowers.sort(key=lambda x:(x[0], x[1])) # x[0]으로 정렬한 후, x[1]으로 한번 더 정렬

print(flowers)

selected=[]
end=60 # 마지막으로 선택된 꽃의 end date

x=-1
temp=0
changed=0
selected=[]

# 마지막 꽃의 end 값이 enddate보다 적거나 같을 때
# flowers의 배열 개수이하로 반복
while end<=enddate and x<N:
    print('진입')
    changed=0
    x+=1
    
    # 반복문 종료: 조건 내에서 가장 큰 end 값 가진 꽃의 인덱스 가져옴
    for i in range(x, N):
        if flowers[i][0]>end: # 해당 꽃의 start date가 end 이후이면 break
            break
        # 해당 꽃의 start date가 end 이전일 때
        if temp<flowers[i][1]: # 조건 중 end date 가장 큰 flower 찾기
            temp=flowers[i][1]
            x=i # flower 인덱스
            changed=1
            
    # end 값 초기화
    if changed==1:
        print('changed')
        end=temp
        selected.append(flowers[x]) # 최대 idx의 flower 삽입

    else: # 안넣으면 마지막에 틀림
        print('not changed')
        selected=[]
        break

print(len(selected))
