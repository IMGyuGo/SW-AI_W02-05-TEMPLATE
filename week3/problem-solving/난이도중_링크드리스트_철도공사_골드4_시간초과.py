# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N : 시작 역의 개수; M : 공사 횟수
station_list = list(map(int, input().split()))

dic = {} # {station 고유번호 : [이전역, 다음역]}
for idx, station in enumerate(station_list) :
  if idx == 0 :
    dic[station] = [ station_list[len(station_list)-1], station_list[idx+1] ]
  elif idx == len(station_list)-1 :
    dic[station] = [ station_list[idx-1], station_list[0] ]
  else :
    dic[station] = [ station_list[idx-1], station_list[idx+1] ]

"""
공사방법
BN i j : i 앞에 있는 역을 출력하고 j 역 설립
BP i j : i 뒤에 있는 역을 출력하고 j 역 설립
CN i : i를 가진 역의 다음 역을 폐쇄하고 폐쇄한 역의 고유 번호 출력
CP i : i를 가진 역의 이전 역을 폐쇄하고 폐쇄한 역의 고유 번호 출력
"""

result = []
def stationPrint(Ch) :
  # C는 공사방법, i는 현재 역, j는 새로 설립할 역
  C, i, j = Ch[0], int(Ch[1]), -1

  if len(Ch) == 3 :
    j = int(Ch[2])

  if C == 'BN' :
    P, N = dic[i] # 현재 역의 이전역과 다음역 가져오기
    P1, N1 = dic[N] # 다음 역의 이전역과 다음역 가져오기
    result.append(N) # 다음 역 출력하기
    dic[i][1] = j # 현재 역의 다음 역을 j역으로 변경
    dic[j] = [i, N] # j역의 이전 역을 i, 다음 역을 N로 생성
    dic[N] = [j, N1] # 다음역의 이전 역을 j, 다음 역을 N1로 변경

  elif C == 'BP' :
    P, N = dic[i] # 현재 역의 이전역과 다음역 가져오기
    P1, N1 = dic[P] # 이전 역의 이전역과 다음역 가져오기
    result.append(P) # 이전 역 출력하기
    dic[i][0] = j # 현재 역의 이전 역을 j역으로 변경
    dic[j] = [P, i] # j역의 이전 역을 P, 다음 역을 i로 생성
    dic[P] = [P1, j] # 이전역의 이전 역을 P1, 다음 역을 j로 변경

  elif C == 'CP' :
    P, N = dic[i] # 현재 역의 이전역과 다음역 가져오기
    P1, N1 = dic[P] # 이전 역의 이전역과 다음역 가져오기
    result.append(P) # 이전 역 출력 하기
    del dic[P] # 이전 역 삭제
    dic[i][0] = P1 # 현재 역의 이전 역을 P1으로 변경
    dic[P1][1] = i # 이이전 역의 다음 역을 i로 변경
    
  else :
    P, N = dic[i] # 현재 역의 이전역과 다음역 가져오기
    P1, N1 = dic[N] # 다음 역의 이전역과 다음역 가져오기
    result.append(N) # 다음 역 출력 하기
    del dic[N] # 다음 역 삭제
    dic[i][1] = N1 # 현재 역의 다음 역을 N1으로 변경
    dic[N1][0] = i # 다다음 역의 이전 역을 i로 변경


# print(dic)
for _ in range(M) :
  # 공사 방법 출력
  C = list(map(str, input().split()))
  stationPrint(C)

print('\n'.join(map(str, result)))