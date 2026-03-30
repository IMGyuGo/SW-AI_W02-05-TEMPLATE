# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

t = int(input())

for _ in range(t):
    n = int(input())
    coins = [i for i in list(map(int, input().split()))]
    m = int(input())
    dp = {i: 0 for i in range(m + 1)}
    dp[0] = 1

    for coin in coins:
        for money in range(coin, m + 1):
            dp[money] += dp[money - coin]

    print(dp[m])
