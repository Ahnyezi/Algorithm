n = int(input())
# 입력된 알파벳 단어를 구성하는 각 알파벳의 인덱스를 추출한다. (idx = 0~25)
# word: 입력값의 알파벳 idx를 담기 위한 배열
# ex) ZY ABC DEF ==> [[25, 24], [0, 1, 2], [3, 4, 5]]
word = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(n)]

# alpha: 각 알파벳의 우선순위를 저장하기 위한 배열 (방 개수 26개 (0~25) )
alpha = [0] * 26
for i in range(n): # 입력값의 개수만큼 반복하여 우선순위 값 설정
    j = 0
    for w in word[i][::-1]: # 저장된 idx를 뒤에서 부터 뽑아서 십진수로 만듦
        alpha[w] += (10 ** j)
        j += 1

alpha.sort(reverse=True) # 우선순위 내림차순으로 정렬

ans, t = 0, 9
for i in range(26):
    if alpha[i] == 0:
        break
    ans += (t * alpha[i])
    t -= 1
print(ans)
