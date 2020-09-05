# 1번
# range까지의 수 중
# 정수 a나 b로 나누어떨어지는 수의 합 구하기

class Solution:
    def solution(self, a, b, k):
        sum = 0
        for num in range(1, k+1):
            if num%a ==0 or num%b ==0:
                sum+=num
        return sum

s = Solution
print(s.solution(s,2,11,22))