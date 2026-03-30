# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

n, m = map(int, input().split())

blocks = set()
for _ in range(m):
    blocks.add(int(input()))

result = n + 1

visited = set()


def jump(prev_jump, cur_step, depth):
    global result

    if cur_step > n:
        return -1
    if cur_step == n:
        return depth

    if cur_step in blocks:
        return -1

    move = prev_jump + 1
    if (cur_step + move, move) not in visited:
        visited.add((cur_step + move, move))
        val = jump(move, cur_step + move, depth + 1)
        if val != -1:
            result = min(val, result)
    move = prev_jump
    if (cur_step + move, move) not in visited:
        visited.add((cur_step + move, move))
        val = jump(move, cur_step + move, depth + 1)
        if val != -1:
            result = min(val, result)
    if prev_jump != 1:
        move = prev_jump - 1
        if (cur_step + move, move) not in visited:
            visited.add((cur_step + move, move))
            val = jump(move, cur_step + move, depth + 1)
            if val != -1:
                result = min(val, result)

    return -1


jump(1, 2, 1)
if n == 2:
    result = 1
if 2 in blocks or result == n + 1:
    result = -1

print(result)
