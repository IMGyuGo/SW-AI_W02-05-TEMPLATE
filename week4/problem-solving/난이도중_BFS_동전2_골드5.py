# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294

import sys
from collections import deque

input = sys.stdin.readline

n, target = map(int, input().split())

coins = set()

for _ in range(n):
    coins.add(int(input()))

coins = list(coins)
coins.sort()

queue = deque()
queue.append(0)
visited = set()


coin_cnt = 0
while queue:

    length = len(queue)
    flag = False

    for _ in range(length):
        coin = queue.popleft()
        for c in coins:
            if coin + c in visited:
                continue
            if coin + c < target:
                queue.append(coin + c)
                visited.add(coin + c)
            elif coin + c == target:
                flag = True
                break
        if flag:
            break
    coin_cnt += 1
    if flag:
        break

    if not queue:
        if not flag:
            coin_cnt = -1

print(coin_cnt)

# while queue:
#     target_list = queue.popleft()

#     tmp_target = target_list[0]
#     coin_cnt = target_list[1]

#     flag = False

#     for c in coins:
#         tmp_target -= c
#         # if tmp_target in visited:
#         #     continue
#         if tmp_target == 0:
#             result = coin_cnt + 1
#             flag = True
#             break
#         elif tmp_target < 0:
#             break
#         queue.append([tmp_target, coin_cnt + 1])
#         # visited.add(tmp_target)
#         tmp_target += c

#     if flag:
#         break

# print(result)

# coins = list(coins)
# heapq.heapify(coins)

# cnt_coins = float("inf")
# while coins:
#     max_coin = -heapq.heappop(coins)

#     cur_coins_cnt = 0

#     cnt = target // max_coin

#     for c in range(cnt):
#         cur_coins_cnt += c

#         remain = target - (max_coin * c)
#         if remain == 0:
#             if cnt_coins > cur_coins_cnt:
#                 cnt_coins = cur_coins_cnt
#                 continue

#         remain_coins = sorted(coins)

#         for r_c in remain_coins:
#             r_c *= -1

#             cnt = remain // r_c
#             cur_coins_cnt += cnt
#             remain = remain % r_c

#             if remain == 0:
#                 if cnt_coins > cur_coins_cnt:
#                     cnt_coins = cur_coins_cnt
#                     break


# if cnt_coins == float("inf"):
#     cnt_coins = -1

# print(int(cnt_coins))
