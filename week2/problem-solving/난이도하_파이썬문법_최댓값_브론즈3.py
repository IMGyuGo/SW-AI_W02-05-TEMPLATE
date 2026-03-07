# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

l1 = [0]*9

for i in range(9) :
  l1[i] = int(input())

max = -1
max_idx = 0
for i, val in enumerate(l1) :
  if max < val :
    max, max_idx = val, i

print(max)
print(max_idx+1)
