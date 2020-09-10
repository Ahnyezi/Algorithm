import sys

if __name__ == "__main__":
    coins = [500,100,50,10,5,1]
    money = int(sys.stdin.readline())
    change = 1000 - money
    count = 0

    while True:
        if change <= 0:
            break
        for c in coins:
            if change >= c:
                change -= c
                count += 1
                break

    print(count)

'''
# 1차시도
import sys

if __name__ == "__main__":
    coins = [500,100,50,10,5,1]
    money = int(sys.stdin.readline())
    change = 1000 - money
    count = 0

    for c in coins:
        if change == 0:
            break
        if change >= c:
            change-=c
            count+=1

    print(count)
'''