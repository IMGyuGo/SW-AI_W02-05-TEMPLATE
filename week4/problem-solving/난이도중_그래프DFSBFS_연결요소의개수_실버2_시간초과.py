# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

from collections import deque

n, m = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
visited = set()
for i in range(1, n + 1):
    visited.add(i)
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

start = 1

queue = deque()

queue.appendleft(start)
visited.remove(1)

result = 0
while queue:
    val = queue.pop()
    next_node = graph[val]

    for n in next_node:
        if n not in visited:
            continue
        else:
            queue.appendleft(n)
            visited.remove(n)

    if not queue:
        result += 1
        if visited:
            queue.appendleft(visited.pop())


print(result)
