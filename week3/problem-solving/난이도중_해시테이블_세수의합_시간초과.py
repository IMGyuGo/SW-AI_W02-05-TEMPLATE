# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

import sys
input = sys.stdin.readline

n = int(input())
group = []
for _ in range(n) :
  group.append(int(input()))

group = sorted(group)

def bt(arr, s, e, target) :

  if len(arr) == 3 :
    if sum(arr) == target :
      return target
    else :
      return -1
  
  for i in range(s, e+1) :
    arr.append(group[i])
    t = bt(arr, i+1, e, target)
    arr.pop()
    if t != -1 :
      return t
    
  return -1


end = len(group)-1

for idx in range(end, 0, -1) :
  result = bt([], 0, idx-1, group[idx])
  if result != -1 :
    print(result)
    break


