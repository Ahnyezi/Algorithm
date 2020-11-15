# LIS
# 1) 최대 몇개 숫자 남길 수 있는지
nums = [1,8,3,2,4,8,3,2,7,6,4,1,3,5,7,6,9,5,4,7,2,8,9]
dp = [1]*len(nums)

for i in range(1,len(nums)):
    flag = False
    max = 0
    for j in range(0,i):
        if nums[i] > nums[j] and dp[max] <= dp[j]: # 앞에서 가장 큰 값 고르기
           flag = True
           max = j
    if flag:
        dp[i] = dp[max] + 1

print(nums)
print(dp)
print(dp[-1])
