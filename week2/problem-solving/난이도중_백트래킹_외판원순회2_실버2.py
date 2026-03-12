# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

n = int(input())

li = [list(map(int, input().split())) for _ in range (n)]

visited = [False]*n # 반복문 방문 체크
min = float('inf')
# now : 현재 도시
# depth : 몇 개의 도시를 방문했는지
# val : 누적 비용

# 시작 도시는 하나로 고정해도 됨
"""
A -> B -> C -> A
B -> C -> A -> B
C -> A -> B -> C
는 같은 사이클임
"""
def tsp(now, depth, val) :
  global min

  if depth == n :
    if min > val :
      min = val

  # 현재 로직은 A에서 부터만 시작
  for i in range(n) :
    # 지역 A 반복문 돌려서 0 이 나오면 패스
    if li[now][i] == 0 :
      continue
    else :
      # 이미 돌린 앞부분이 이미 간 부분이면 넣고 빼기
      if visited[i] :
        pass
      else :
        visited[i] = True
        val += li[now][i]
        tsp(i, depth+1, val)
        val -= li[now][i]
        visited[i] = False

tsp(0, 0, 0)

print(min)