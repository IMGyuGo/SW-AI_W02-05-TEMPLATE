# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

# 현재 위치의 값이 결승점까지의 거리보다 멀 경우는 못감
# 현재 위치의 값이 결승점까지의 거리와 같을 경우 HaruHaru
# 현재 위치의 값이 결승점보다 적을 경우 재귀로 확인

n = int(input())
jump_map = [list(map(int, input().split())) for _ in range(n)]


def bfs(ary, row, col):

    result = "Hing"

    val = ary[row][col]
    if val == 0:
        return "Hing"
    distance = 2 * n - row - col - 2
    if val < distance:
        for i in range(val + 1):
            row_plus = row + i
            col_plus = col + val - i
            if row_plus >= n or col_plus >= n:
                continue
            result = bfs(ary, row_plus, col_plus)
            if result == "HaruHaru":
                return result
    elif val > distance:
        return "Hing"
    else:
        return "HaruHaru"

    return result


print(bfs(jump_map, 0, 0))
