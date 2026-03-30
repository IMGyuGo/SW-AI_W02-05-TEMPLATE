# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

dp = {i: 0 for i in range(k + 1)}
items = {}
for _ in range(n):
    w, v = map(int, input().split())
    if v == 0:
        continue
    if w <= k:
        items[w] = v

for w in items:
    for j in range(k, w - 1, -1):
        v = items[w]
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[k])
