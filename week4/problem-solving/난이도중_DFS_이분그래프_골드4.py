# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 이것 처리 해줘야 재귀 1000 제한을 넘을 수 있음
from collections import deque

t = int(input())
for _ in range(t):
    v, e = map(int, input().split())

    node_list = {i: [] for i in range(1, v + 1)}
    for _ in range(e):
        fir, sec = map(int, input().split())

        node_list[fir].append(sec)
        node_list[sec].append(fir)

    dp = [None] * (v + 1)

    def dfs(start, binary):

        nxt = node_list[start]
        if dp[start] == None:
            if binary:
                dp[start] = 0
            else:
                dp[start] = 1

        binary = dp[start]

        for n in nxt:
            if dp[n] == None:
                result = dfs(n, binary)
                if result == False:
                    return False
            else:
                if dp[start] == dp[n]:
                    return False
        return True

    result = True
    for i in range(1, v + 1):
        if dp[i] is None:
            if not dfs(i, 1):
                result = False
                break

    if result:
        print("YES")
    else:
        print("NO")
