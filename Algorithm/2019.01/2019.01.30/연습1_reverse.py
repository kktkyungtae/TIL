# 문자열 뒤집기
# Reverse 함수 혹은 slice natation을 이용해서 구현하면 된다.

s = 'Reverse ths strings'
sr =''

for i in range(len(s)-1, -1, -1):
    sr = sr + s[i]

print(sr)