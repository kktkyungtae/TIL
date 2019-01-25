# 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
#
# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
#
# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.

T = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
ca = 0
cb = 0
co = 0
cab = 0
for i in T:
    if i == 'A':
        ca +=1
    elif i == 'B':
        cb +=1
    elif i == 'O':
        co +=1
    else:
        cab +=1

