# 다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오.

yak = int(input())

for i in range(1,yak+1):
    if yak % i == 0:
        print(f'{i}(은)는 {yak}의 약수입니다.')
    else:
        i+=1
