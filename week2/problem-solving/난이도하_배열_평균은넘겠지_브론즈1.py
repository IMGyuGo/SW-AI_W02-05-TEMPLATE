# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

C = int(input())
for _ in range(C) :
  nums = list(map(int, input().split()))
  n = nums[0]
  scores = nums[1:]

  mean = sum(scores)/n
  up = 0
  for score in scores :
    if mean < score :
      up+=1
  
  percent = up / float(n) * 100
  print(f"{percent:.3f}%")