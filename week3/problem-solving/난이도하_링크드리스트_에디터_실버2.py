# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

import sys
input = sys.stdin.readline

text = input().rstrip()
m = int(input())

# nodes[node_id] = [char, prev, next]
nodes = {}

head = 0         # 첫 번째 노드 id
tail = 0         # 마지막 노드 id
cursor = 0       # 커서 왼쪽 노드 id
node_id = 1

# 초기 문자열로 연결리스트 만들기
prev = 0
for ch in text:
    nodes[node_id] = [ch, prev, 0]

    if prev != 0:
        nodes[prev][2] = node_id
    else:
        head = node_id

    prev = node_id
    cursor = node_id   # 초기 커서는 맨 뒤
    tail = node_id
    node_id += 1

for _ in range(m):
    cmd = input().split()

    if cmd[0] == 'L':
        if cursor != 0:
            cursor = nodes[cursor][1]

    elif cmd[0] == 'D':
        if cursor == 0:
            if head != 0:
                cursor = head
        else:
            nxt = nodes[cursor][2]
            if nxt != 0:
                cursor = nxt

    elif cmd[0] == 'B':
        if cursor != 0:
            delete_id = cursor
            prev_id = nodes[delete_id][1]
            next_id = nodes[delete_id][2]

            if prev_id != 0:
                nodes[prev_id][2] = next_id
            else:
                head = next_id

            if next_id != 0:
                nodes[next_id][1] = prev_id
            else:
                tail = prev_id

            cursor = prev_id
            del nodes[delete_id]

    elif cmd[0] == 'P':
        ch = cmd[1]
        new_id = node_id
        node_id += 1

        if cursor == 0:
            # 맨 앞에 삽입
            next_id = head
            nodes[new_id] = [ch, 0, next_id]

            if head != 0:
                nodes[head][1] = new_id
            else:
                tail = new_id

            head = new_id
            cursor = new_id

        else:
            prev_id = cursor
            next_id = nodes[prev_id][2]

            nodes[new_id] = [ch, prev_id, next_id]
            nodes[prev_id][2] = new_id

            if next_id != 0:
                nodes[next_id][1] = new_id
            else:
                tail = new_id

            cursor = new_id

# 결과 출력
answer = []
cur = head
while cur != 0:
    answer.append(nodes[cur][0])
    cur = nodes[cur][2]

print(''.join(answer))