# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

items = []
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

queue = deque()
queue.append((0, 0))

dp = {}
queue = deque()
for i in range(n):
    w, v = items[i]
    queue.append((w, v, {(w, v)}))

max_val = 0
while queue:
    w, v, visited = queue.popleft()
    if w <= k:
        dp[w] = max(v, dp[w] if w in dp else 0)
        if max_val < dp[w]:
            max_val = dp[w]

    for item in items:
        if item in visited:
            continue
        else:
            w1 = item[0]
            v1 = item[1]
            if w + w1 <= k:
                visited.add(item)
                queue.append((w + w1, v + v1, visited))
                visited.remove(item)

print(max_val)
