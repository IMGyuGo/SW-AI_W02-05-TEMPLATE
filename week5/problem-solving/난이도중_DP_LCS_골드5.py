# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251

first = list(" " + input())
second = list(" " + input())

row = len(first)
col = len(second)

dp = [[0 for _ in range(col)] for _ in range(row)]

max_val = 0
for i in range(row):
    for j in range(col):
        if i != 0 and j != 0:
            if first[i] == second[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_val:
                    max_val = dp[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(max_val)
