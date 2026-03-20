# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

n, m = map(int, input().split())

for i in range(n):
    if i == 0:
        for j in range(1, m + 1):
            print(i, j)
    elif i <= m:
        continue
    else:
        print(i - 1, i)
