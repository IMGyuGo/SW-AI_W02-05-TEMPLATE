# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056

from collections import deque

n = int(input())
time = [0] * (n + 1)
next_work = {i: [] for i in range(1, n + 1)}
indegree = [0] * (n + 1)
dp = [0] * (n + 1)


for idx in range(n):
    work = list(map(int, input().split()))
    t = work[0]
    adv_cnt = work[1]
    indegree[idx + 1] = adv_cnt
    for i in range(2, 2 + adv_cnt):
        next_work[work[i]].append(idx + 1)

    time[idx + 1] = t

queue = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = time[i]

while queue:
    cur = queue.popleft()

    for nxt in next_work[cur]:
        dp[nxt] = max(dp[nxt], dp[cur] + time[nxt])
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            queue.append(nxt)

print(max(dp))

# start = adv_work[1]
# running_time = time[1]


# def bfs(start, running_time):

#     running_time_list = []

#     for s in start:
#         adv = adv_work[s]
#         nxt = next_work[s]

#         for n in nxt:
#             visited[n] = True
#             running_time_list.append(time[n])

#         running_time += max(running_time_list)
#         bfs(adv, running_time)


# def dfs(start, running_time):

#     for a in adv_work[start]:
#         if visited[a]:
#             continue
#         else:
#             return 0

#     nxt = next_work[start]
#     visited[start] = True
#     t = 0
#     for n in nxt:
#         running_time -= t
#         t = dfs(n, running_time + time[start])
#         running_time += t

#     return running_time


# while queue:
#     cur = queue.pop()
#     adv = adv_work[cur]
#     nxt = next_work[cur]

#     for a in adv:
#         if visited[a]:
#             adv.remove(a)

#     if len(adv) != 0:
#         continue
#     else:
#         result += time[cur]
#         for n in nxt:
#             queue.appendleft(n)
