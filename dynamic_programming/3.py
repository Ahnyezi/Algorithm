# LIS
# 2) 가장 큰 증가하는 부분 수열
# 남은 수열의 합의 최대값 구해라

nums = [1,8,3,2,4,8,3,2,7,6,4,1,3,5,7,6,9,5,4,7,2,8,9]
dp = [0]*len(nums)

for i in range(0,len(nums)):
    flag = False
    max_nums = 0
    for j in range(0,i):
        if nums[i] > nums[j] and max_nums <= dp[j]: # 조건 주의
            max_nums = dp[j]
            flag = True
    if flag:
        dp[i] = max_nums + nums[i]
    else:
        dp[i] = nums[i]

print(nums)
print(dp)
print(max(dp))
