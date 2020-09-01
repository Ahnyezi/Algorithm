import sys

change = 1000 - int(sys.stdin.readline())
coins = [500,100,50,10,5,1]
count = 0

for c in coins:
    count += change//c
    change %= c

print(count)
