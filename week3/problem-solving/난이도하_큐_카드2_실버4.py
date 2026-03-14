# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

from collections import deque

n = int(input())

queue = deque()

for i in range(1, n+1) :
  queue.append(i)

order = 1
while len(queue) != 1 :
  if order % 2 != 0 :
    queue.popleft()
  else :
    queue.append(queue.popleft())

  order += 1

print(queue.pop())