# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

n = int(input())
for _ in range(n) :
  q = input().split()
  iterNum = int(q[0])
  text = q[1]

  textList = text[:]

  result = ""
  for t in textList :
    result += t*iterNum

  print(result)