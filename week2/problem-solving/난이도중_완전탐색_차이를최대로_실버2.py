# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

# 가장 큰 수와 가장 작은 수 가장 큰 수(두번째)로 시작

n = int(input())
li = list(map(int, input().split()))

visited = [False] * n
max = 0
def dfs(visited, depth, s, e, result) :
  global max

  if depth == n :
    if max < result :
      max = result
    return

  t_e = e
  t_result = result

  for i in range(n) :
    if visited[i] == False :
      visited[i] = True
      if depth == 0 :
        dfs(visited, depth+1, li[i], 0, 0)
      else :
        e = li[i]
        result += abs(s-e)
        dfs(visited, depth+1, e, 0, result)
      visited[i] = False
      e = t_e
      result = t_result
    


dfs(visited, 0, 0, 0, 0)

print(max)