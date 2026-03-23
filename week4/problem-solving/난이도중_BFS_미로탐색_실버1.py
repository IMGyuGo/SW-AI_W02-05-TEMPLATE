# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    tmp_li = list(map(int, list(input())[:-1]))
    graph.append(tmp_li)

dp = []
visited = []
for _ in range(n):
    dp.append([0 for _ in range(m)])
    visited.append([False for _ in range(m)])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

start = (0, 0)
queue = deque()
queue.append(start)
dp[0][0] = 1
visited[0][0] = True

while queue:
    cord = queue.popleft()
    if len(cord) != 2:
        prev_dir = (cord[2][0] * -1, cord[2][1] * -1)
    for d in dirs:
        if len(cord) != 2:
            if d == prev_dir:
                continue
        row = cord[0] + d[0]
        col = cord[1] + d[1]

        if row < 0 or col < 0:
            continue
        if row > n - 1 or col > m - 1:
            continue
        if graph[row][col] == 0:
            continue
        if visited[row][col]:
            continue
        if dp[row][col] == 0:
            dp[row][col] = dp[cord[0]][cord[1]] + 1
        else:
            dp[row][col] = min(dp[row][col], dp[cord[0]][cord[1]] + 1)

        queue.append((row, col, d))
        visited[row][col] = True

print(dp[n - 1][m - 1])


# def dfs(left, right, res):
#     global result

#     val = graph[left][right]

#     if left == n - 1 and right == m - 1:
#         res += 1
#         if result > res:
#             result = res
#         return False

#     if val == 0:
#         return False

#     res += 1
#     if left != n - 1:
#         dfs(left + 1, right, res)
#     if right != m - 1:
#         dfs(left, right + 1, res)


# dfs(0, 0, 0)
