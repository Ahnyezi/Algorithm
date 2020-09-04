import sys
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

negative = []
positive = []
ans = 0

for num in nums:
    if num <= 0:    # 0도 negative의 원소로 둠
        negative.append(num)
    elif num == 1:  # 1인 경우에는 묶지 않고 더함
        ans += 1
    elif num > 1:
        positive.append(num)

# 목적에 맞게 정렬
negative.sort()
positive.sort(reverse=True)

# 1) 작은 수부터 차례로 묶음
for i in range(0,len(negative),2):
    if i+1 < len(negative):
        ans += negative[i]*negative[i+1]
    else:
        ans += negative[i]

# 2) 큰 수부터 차례대로 묶음
for i in range(0,len(positive),2):
    if i+1 < len(positive):
        ans += positive[i]*positive[i+1]
    else:
        ans += positive[i]

print(ans)

# 알고리즘 정리
# 1) 0을 포함한 음수는 작은 수부터 묶음 ex.(-5*-4) (-3*-2) => 정방향 정렬
# 2) 1은 묶지 않음
# 3) 양수는 큰 수부터 묶음 ex. (5*4) (3*2) => 역방향 정렬

# 틀린 이유: 통일 못함
# 1) case 통일해서 생각 못함
# 1-a. 1은 어떤 경우에서든 곱셈 없이 더함
# 1.b. 0은 양수 쪽에서는 영향 없지만, 음수 쪽에서는 곱해준다.
# 2) 홀수/짝수 함께 처리할 수 있는 알고리즘
# i에 조건을 걸어주기: if i < len(list) -1