# 1부터 100까지의 숫자를 for 문과 range 함수를 이용해 출력하십시오.


a =[]
for i in range(1,101):
    if i % 2 !=0:
        a.append(i)

for j in range(len(a)):
    if j != len(a)-1:
        print(a[j], end = ", ")
    else:
        print(a[j])