# 다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오
# (단, 약수가 2개일 경우 소수임을 나타내십시오)

yak = int(input())
j=[]

for i in range(1,yak+1):
    if yak % i == 0:
        j.append(i)
        print(f'{i}(은)는 {yak}의 약수입니다.')


if len(j) == 2:
    print(f'{i}(은)는 {j[0]}과 {j[1]}로만 나눌 수 있는 소수입니다.')
