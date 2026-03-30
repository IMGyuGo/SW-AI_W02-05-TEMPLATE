# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

import sys
from collections import deque

input = sys.stdin.readline

dp = {}

n, k = map(int, input().split())

items = []
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

items.sort()

queue = deque()
queue.append((0, 0))

dp = {}

max_val = 0


def bt(weight, value, visited):
    global max_val

    for item in items:
        if item not in visited:
            if weight + item[0] > k:
                break
            visited.add(item)
            dp[weight + item[0]] = max(
                value + item[1], dp[weight + item[0]] if weight + item[0] in dp else 0
            )
            if dp[weight + item[0]] > max_val:
                max_val = dp[weight + item[0]]
            bt(weight + item[0], value + item[1], visited)
            visited.remove(item)


bt(0, 0, set())
print(max_val)
