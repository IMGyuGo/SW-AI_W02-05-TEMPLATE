# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

import math

n = int(input())
li = [[] for _ in range(n)]
min = 2100000000
route = []*n
