list = []
n = int(input())
max = 0
cnt = 0

for i in range(0,n):
    info = input()
    hours = int(info.split(" ")[1]) - int(info.split(" ")[0])
    if int(info.split(" ")[1]) > max:
        max = int(info.split(" ")[1])
    list.append((info, hours))
print(list)

room = [0 for i in range(max+1)] #오류2) max+1
# print(room)

for i in range(0,n-1):
    min_idx = i
    for j in range(i+1,n):
        if(list[min_idx][1] > list[j][1]):
            min_idx = j
    list[i],list[min_idx] = list[min_idx],list[i]
print(list)

for i in range(0,n):
    # print(i)
    start = int(list[i][0].split(" ")[0])
    end = int(list[i][0].split(" ")[1])
    print(start,"/",end)
    if start == end:
        if room[i] < 1:
            room[i] += 1
            cnt += 1
            print('cnt:',cnt)
            print('room:', room)
        continue
    # check
    flag = True
    for j in range(start,end+1):
        if room[j] > 0: # 조건 오류) room[j] < 2
            flag = False
            break
    # insert
    if flag:
        for j in range(start+1,end): # 조건: start, end+1
            room[j]+=1
        cnt += 1
        print('cnt 2:', cnt)
        print('room:',room)

print(cnt)
