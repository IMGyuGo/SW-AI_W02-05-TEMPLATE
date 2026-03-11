# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

n = int(input())

# 핵심 : 퀸을 놓을 때, 열만 생각하면 된다. 무조건 한 행에 한개만 배치하는 구조이기 때문에

count = 0
li = [0] * n

def check_queen(row, col) :
  for i in range(row) :
    if li[i] == col :
      return False
    elif abs(row-i) == abs(col-li[i]) :
      return False
  return True
  
def queen(row) :
  global count

  if row == n :
    count += 1
    return
  
  for col in range(n) :
    if check_queen(row, col) :
      li[row] = col
      queen(row+1)

queen(0)
print(count)