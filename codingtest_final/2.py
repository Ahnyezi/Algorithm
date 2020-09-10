# 2번. 막대의 개수 구하기
# 최초의 길이 64에서 x로 만들었을 때 막대의 개수

# 막대 부수는 방법
# 1. 가장 짧은 길이 막대를 반으로 나눔
# 2. 나머지 막대와 가장 작은 막대 1/2한 합이 x보다 크거나 같으면, 가장 짧은 막대의 1/2를 버림
# 3. x = 나머지 막대들 + 가장 짧은 막대 1/2 로 초기화

# 0 :64
# 1: 32, 32
# 2: 32, 16=> if 32+16 == x, return 2
# 3: 32, 8, ==> if 32+8 == x, return 3

class Solution:
    def solution(self, x):
        sticks = [64]
        ans = 0
        if x == 64: return 1 # 예외처리
        while True:
            last = sticks[-1]
            if sum(sticks)-last/2 > x: # 가장 작은 막대 1/2한 합이 x보다 크면, 최소 막대 1/2 버림
                sticks[-1] = last/2
            elif sum(sticks)-last/2 < x: # 작으면, 현재 가장작은 막대 pop하고, 가장 작은 막대 1/2한 값 두개를 리스트에 붙임
                sticks.pop()
                sticks.append(last / 2)
                sticks.append(last / 2)
            else: # 같으면 해당 시행의 막대 개수 반환
                ans = len(sticks)
                break
        return ans

s = Solution
print(s.solution(s,64))