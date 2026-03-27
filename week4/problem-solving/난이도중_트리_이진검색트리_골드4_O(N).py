# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

import sys

sys.setrecursionlimit(10**6)  # 이것 처리 해줘야 재귀 1000 제한을 넘을 수 있음
input = sys.stdin.readline

preorder = []
for line in sys.stdin:
    preorder.append(int(line.strip()))

idx = 0
n = len(preorder)
result = []


def build(lower, upper):
    global idx

    if idx >= n:
        return

    cur = preorder[idx]

    # 현재 값이 이 서브트리에 들어올 수 없는 값이면 종료
    if not (lower < cur < upper):
        return

    # 현재 값을 루트로 사용
    idx += 1

    # 왼쪽 서브트리
    build(lower, cur)

    # 오른쪽 서브트리
    build(cur, upper)

    # 후위 순회이므로 마지막에 루트 추가
    result.append(cur)


build(float("-inf"), float("inf"))

print("\n".join(map(str, result)))
