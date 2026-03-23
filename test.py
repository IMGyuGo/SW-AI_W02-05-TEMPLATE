# 전위
# 루트,왼쪽,오른쪽
# 중위
# 왼쪽,루트,오른쪽
# 후위
# 왼쪽,오른쪽,루트

n = int(input())
dic = {}
for _ in range(n):
    node, left, right = input().split()

    dic[node] = []
    dic[node].append(left)
    dic[node].append(right)

start = "A"

f_order_list = []


def f_order(start):

    left = dic[start][0]
    right = dic[start][1]

    f_order_list.append(start)

    if left != ".":
        f_order(left)

    if right != ".":
        f_order(right)


m_order_list = []


def m_order(start):
    left = dic[start][0]
    right = dic[start][1]

    if left != ".":
        m_order(left)
    m_order_list.append(start)
    if right != ".":
        m_order(right)


p_order_list = []


def p_order(start):

    left = dic[start][0]
    right = dic[start][1]

    if left != ".":
        p_order(left)
    if right != ".":
        p_order(right)
    p_order_list.append(start)


f_order("A")
m_order("A")
p_order("A")

print("".join(f_order_list))
print("".join(m_order_list))
print("".join(p_order_list))

"""
     A
  B   C
 D . E   F
. . . . . G
         . .
"""
