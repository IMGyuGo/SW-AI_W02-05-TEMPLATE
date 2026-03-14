# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.readline

n = int(input())

stack = []

def push_command(X) :
  stack.append(X)

def command(s) :
  if s == "pop" :
    if len(stack) == 0 :
      return -1
    else :
      return stack.pop()
  if s == "size" :
    return len(stack)
  if s == "empty" :
    if len(stack) == 0 :
      return 1
    else :
      return 0
  if s == "top" :
    if len(stack) == 0 :
      return -1
    else :
      return stack[len(stack)-1]

for _ in range(n) :
  text = input().split()

  if len(text) == 1 :
    print(command(text[0]))
  else :
    push_command(text[1])