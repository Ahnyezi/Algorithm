# 3. 문자열 정돈하기
# 느낌표-물음표 연속 ==> 하나의 물음표로 바꾸기
# 느낌표-느낌표 연속 ==> 하나의 느낌표로 바꾸기

class Solution:
    def solution(self, document):
        d = list(document)
        prev = '0'
        i = 0
        while i < len(d):
            ch = d[i]
            if (prev == '!' and ch == '?') or (prev =='!' and ch == '!') or (prev =='?' and ch == '?') :
                i -= 1
                d.pop(i)
            elif (prev == '?' and ch == '!'):
                d.pop(i)
                i -= 1
            prev = d[i] # prev 매시행마다 변화!
            i+=1

        return "".join(d)

s = Solution
# ans = s.solution(s," a b c A B ! !!C!!! ! ! !C ?!!? ?!? ??")
ans = s.solution(s,"a??a ?!a a!?b b!?!C C?!!D D?!?EE ??? FF!!! !???!")
# if ans == " a b c A B ! !C! ! ! !C ? ? ?":
if ans == "a?a ?a a?b b?C C?D D?EE ? FF! ?":
    print('정답')
else:
    print('오답')
    print(ans)
    print("a?a ?a a?b b?C C?D D?EE ? FF! ?")