# LCS

# 1차 틀렷..?
# - 런타임 
# - 틀림
# AACGGAACACGCTTTAAGGGCGATGGAATACCGTGGGTTTACCTAAAACTA
# AATCTGGCCTATTCTGGGTCAAATGGCGTGAGCAAACATCGTACA
# answer:31

import sys
A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1 # **************
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

for i in range(len(dp)):
    print(dp[i])

print(dp[len(A)][len(B)])