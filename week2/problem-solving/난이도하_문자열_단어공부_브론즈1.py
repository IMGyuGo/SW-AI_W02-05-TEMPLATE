# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

text = input()
text = text.upper()
textList = text[:]

info = {}
for i in range(len(textList)) :
  if textList[i] in info.keys() :
    info[textList[i]] += 1
  else :
    info[textList[i]] = 1

max = max(info.values())

result = ''
dupli = 0
for k in info.keys() :
  if info[k] == max :
    dupli+=1
    result = k

if dupli != 1 :
  print('?')
else :
  print(result)

# max값을 구하고
# 중복값이 있으면 ?
# 없으면 그 max 값의 위치