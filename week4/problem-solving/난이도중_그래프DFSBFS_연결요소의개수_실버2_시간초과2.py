# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

from collections import deque

n, m = map(int, input().split())

result_list = [set()]
for i in range(m):
    s, e = map(int, input().split())
    if i == 0:
        result_list[0].add(s)
        result_list[0].add(e)
    else:
        idx = len(result_list) - 1

        for j in range(idx + 1):
            if j == idx:
                if s not in result_list[j] and e not in result_list[j]:
                    result_list.append(set())
                    result_list[-1].add(s)
                    result_list[-1].add(e)
            if s not in result_list[j] and e not in result_list[j]:
                continue
            else:
                result_list[j].add(s)
                result_list[j].add(e)

result = len(result_list)
dp = set()
while True:
    for i in range(len(result_list)):
        if i in dp:
            continue
        fir = result_list[i]
        for j in range(len(result_list)):
            if i == j:
                continue
            if j in dp:
                continue
            sec = result_list[j]

            if fir & sec:
                result_list[i] = fir | sec
                dp.add(j)
                result -= 1
    break

print(result)
