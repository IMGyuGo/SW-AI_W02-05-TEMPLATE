# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493


from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
top = deque(map(int, input().split()))
for i in range(len(top)) :
  top[i] = (top[i], i+1)

result= [0] * n # 정답
def tower(rem) :

  if len(rem) == 0 :
    return

  v = rem.pop() # 초기 탑 값
  h1, idx1 = v # 이전 탑 튜플 언패킹

  if len(rem) == 0 :
    result[idx1-1] = 0
    return

  rest = deque()
  while len(rem) != 0 :
    t = rem.pop() # 비교할 앞 탑
    h2, idx2 = t # 현재 탑
    h1, idx1 = v # 이전 탑

    if h2 >= h1 : # 현재 탑이 더 크면 레이저 인지
      result[idx1-1] = idx2
    else :
      rest.appendleft(v)

    if len(rem) == 0 :
        rest.appendleft(t)

    v = t # 대체

  # while 끝나면 재귀
  tower(rest)

# 초기에 값 정리
while True :
  tmp = top[0]
  tmp_h, tmp_idx = tmp 
  tmp2 = top[1]
  tmp_h2, tmp_idx2 = tmp2
  if tmp_h < tmp_h2 :
    result[tmp_idx] = 0
    top.popleft()
  else :
    break

tower(top)

print(' '.join(map(str, result)))