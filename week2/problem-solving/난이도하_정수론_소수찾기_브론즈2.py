# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

n = int(input())
nums = map(int, input().split())


import math

result = 0
for i in nums :
  if i == 1 :
    continue
  elif i == 2 :
    result += 1
    continue
  flag = True
  for j in range(2, int(math.sqrt(i))+1) :
    if i % j == 0 :
      flag = False
      break
  if flag : result+=1
    
print(result)
