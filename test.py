import sys
input = sys.stdin.readline

n = int(input())

# col[row] = col
col = [-1] * n

answer = 0

used_col = [False] * n
used_diag1 = [False] * (2*n)
used_diag2 = [False] * (2*n)

def backtrack(row):
    global answer
    if row == n:
        answer += 1
        return

    for c in range(n):

        d1 = row - c + (n - 1)
        d2 = row + c

        if used_col[c] or used_diag1[d1] or used_diag2[d2]:
            continue

        used_col[c] = True
        used_diag1[d1] = True
        used_diag2[d2] = True

        backtrack(row + 1)

        used_col[c] = False
        used_diag1[d1] = False
        used_diag2[d2] = False


backtrack(0)
print(answer)