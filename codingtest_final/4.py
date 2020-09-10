# 4. 펠린드롬 만들기
class Solution:
    def palindrome(self, word):
        for i in range(len(word) // 2):
            if word[i] != word[-1 - i]:
                return False
        return True

    def solution(self, s):
        # 모든 문자가 다른 경우
        chars = list(set(s))
        if len(chars) == len(s):
            return len(s)*2-1
        flag = self.palindrome(self,s)
        
        if flag: # 이미 펠린드롬인 경우
            return len(s)
        
        else: # 펠린드롬 아닌 경우
            k = 0
            prev = s[-1]
            for i in range(-1,-len(s),-1):
                if prev == s[i]:
                    k = i
                    prev = s[i]
                else:
                    break
            chars = s # 문자열 s는 길이가 변화하기 때문에
            for i in range(k-1,-len(s)-1,-1):
                s += chars[i % len(chars)] # 고정된 chars 리스트로 처리
                print(s)
                if self.palindrome(self,s) == True:
                    return len(s)

s = Solution
print(s.solution(s,"abcda")) #abcddcba
# print(s.palindrome("abacaba"))