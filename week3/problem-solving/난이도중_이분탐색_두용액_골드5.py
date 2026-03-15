# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

# 산성용액 1 ~ 10억
# 알칼리성용액 -1 ~ -10억
# N은 1 ~ 10^5

n = int(input())
drug = list(map(int, input().split()))


# 정렬
# +와 -로 분할 후, +만 존재하면 +끼리만 더하고 -만 존재하면 -끼리만 더하는 형태니까 3가지로 분할
drug = sorted(drug)

# +일경우와 -일경우 조건을 다르게 줘야 함.
# TODO -> 이분탐색
def binarySearch(arr, s, e, target) :
  # 이진트리 s, e, target
  # 절댓값으로 계산
  mid = (s + e) // 2
  if arr[mid] < target :
    pass

  pass

result = []
plusList = []

if drug[0] >= 0 : # +만 존재
  result.append(drug[0])
  result.append(drug[1])
elif drug[n-1] <= 0 : # -만 존재
  result.append(drug[n-1])
  result.append(drug[n-2])
else :
  # 먼저 +들을 plusList에 큰값부터 순차적으로 저장 pop()할 때 작은 값부터 뽑아 낼 수 있도록
  for idx in range(len(drug)-1, -1, -1) : # 반대로 돌려서 +를 pop으로 뽑아내기 (list로 구현 해놓았기 때문)
    if plusList[idx] > 0 :
      plusList.append(plusList.pop())
    else :
      break

  # 분할정복 (이진분할탐색)
  if len(plusList) <= len(drug) : # -가 +보다 많다면
    for p in plusList :
      min = 1000000000
      # 이진탐색트리 가동 (drug로)
      pass
    for d in drug :
      min = 1000000000
      # 이진 탐색트리 가동 (plusList로)
      pass