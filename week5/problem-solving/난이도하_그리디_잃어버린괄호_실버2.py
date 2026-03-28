# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

# -를 기준으로 split
# - 뒤에 있는것을 괄호로 묶고 계산하면 끝
# 제일 첫번째 있는 것은 +인지 -인지를 체크 해야함.

problem = input()

result = 0
flag = False
if problem.startswith("-"):
    flag = True

minus_problem = problem.split("-")

for idx, m_p in enumerate(minus_problem):
    numbers = map(int, m_p.split("+"))
    if idx == 0 and not flag:
        for number in numbers:
            result += number
        continue
    for number in numbers:
        result -= number

print(result)
