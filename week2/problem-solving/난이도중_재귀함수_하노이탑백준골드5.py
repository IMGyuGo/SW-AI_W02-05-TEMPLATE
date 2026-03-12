# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914


# 1. 위에 있는 n-1개를 A에서 B로 옮긴다
# 2. 가장 큰 원반 1개를 A에서 C로 옮긴다
# 3. B에 있던 n-1개를 B에서 C로 옮긴다

# 보통 함수 인자는 이렇게 잡음
n = int(input())

def hanoi(n, start, via, end) :

  if n == 1 :
    print(start, end)
    return
  
  hanoi(n-1, start, end, via)

  print(start, end)

  hanoi(n-1, via, start, end)

hanoi(n, 1, 2, 3)