# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    start = 0
    airplane = {i: [] for i in range(1, n + 1)}
    for idx in range(m):
        s, e = map(int, input().split())
        if idx == 0:
            start = s
        airplane[s].append(e)
        airplane[e].append(s)

    visited = [start]
    queue = deque()
    queue.appendleft(start)
    result = 0

    while len(queue) != 0:
        vertice = queue.pop()
        airList = airplane[vertice]
        for a in airList:
            if a in visited:
                continue
            else:
                queue.appendleft(a)
                visited.append(a)
                result += 1

    print(result)


# 개선 방법 : visited를 set으로 변경
# 와.... 연결리스트 일 때 정답이 print(n-1) 이라고 한다.. 무조건
