## 문제1번
range까지의 수 중 정수 a나 b로 나누어떨어지는 수의 합 구하기<br>

## 문제2번 | 막대의 개수 구하기
최초의 길이 64에서 x로 만들었을 때 막대의 개수<br>

막대 부수는 방법 <br>
1. 가장 짧은 길이 막대를 반으로 나눔
2. 나머지 막대와 가장 작은 막대 1/2한 합이 x보다 크거나 같으면, 가장 짧은 막대의 1/2를 버림
3. x = 나머지 막대들 + 가장 짧은 막대 1/2 로 초기화


## 문제3번 | 문자열 정돈하기
느낌표-물음표 연속 ==> 하나의 물음표로 바꾸기 <br>
느낌표-느낌표 연속 ==> 하나의 느낌표로 바꾸기

## 문제4번 | 펠린드롬 만들기 (4번 테스트케이스 통과못함..) 왜?
정답
``` python
class Solution:
    def isPalindrome(self, s):
        s_reverse = ''.join(list(reversed(list(s))))
        if s == s_reverse:
            return True
        else:
            return False
            
    def solution(self, s):
        flag = self.isPalindrome(s)
        if not flag:
            for i in range(len(s)):
                s_reverse = ''.join(list(reversed(list(s[:i]))))
                if self.isPalindrome(s + s_reverse):
                    return len(s + s_reverse)
        return len(s)
```
