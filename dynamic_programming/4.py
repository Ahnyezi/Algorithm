# LCS
# 두 문자열 A,B에 대해 A와 B의 공통 부분 문자열 중 가장 길이가 긴 문자열의 길이를 구해라

def lcs(A,B):
    dp = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]
    for i in range(len(A)+1):
        for j in range(len(B)+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]+ 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    for i in range(len(dp)):
        print(dp[i])
    return dp[-1][-1]

A,B = 'apple','elppa'
print("Length of LCS is ",lcs(A,B))