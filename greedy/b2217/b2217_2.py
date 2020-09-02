import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    arr = []

    for i in range(N):
        arr.append(int(input()))
    arr.sort(reverse=True)

    m = 0
    for i in range(len(arr)):
        temp_max = arr[i] * (i+1)
        if temp_max > m:
            m = temp_max

    print(m)