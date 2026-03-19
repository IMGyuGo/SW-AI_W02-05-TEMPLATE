# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

# (A x B) mod C = (A mod C) x (B mod C) mod C (증명 필요!)
A, B, C = map(int, input().split())

# 10^11 => 10 x (10^5)^2
def multiple(A, B, C) :
  if B == 1 :
    return A % C
  # 짝수
  tmp = multiple(A,B//2,C) % C
  if B % 2 == 0 :
    return (tmp * tmp) % C
  # 홀수
  else :
    return (A * tmp * tmp) % C
  
print(multiple(A, B, C))